import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import json
from frontend.api_client import make_request

def render_globe_view():
    st.markdown('<div class="gradient-header">Interactive 3D GeoVerse Globe</div>', unsafe_allow_html=True)
    st.markdown("Explore global geography layers, terrain features, and UPSC study cards on our interactive 3D Earth.")

    # Fetch country summaries
    countries_data = make_request("GET", "/api/countries")
    if not countries_data:
        st.info("Loading seed data. Run database seeder to populate geography records.")
        return

    df = pd.DataFrame(countries_data)

    # Sidebar parameters inside main panel cols or Streamlit expander
    col_globe, col_controls = st.columns([3, 1])

    with col_controls:
        st.markdown("### Layer Settings")
        selected_layer = st.selectbox(
            "Globe Overlay Layer",
            ["Political & Continents", "Climate Zones (Köppen)", "Population Density Heatmap", "GDP / Wealth Distribution"]
        )

        st.markdown("### Toggle Details")
        show_capitals = st.checkbox("Show Capital Cities", value=True)
        show_mountains = st.checkbox("Show Mountain Peaks", value=False)
        show_minerals = st.checkbox("Show Key Mining Deposits", value=False)

        # Fly-to controls
        st.markdown("### Fly-to Country")
        search_country = st.selectbox("Search & Center Globe", ["-- Select --"] + sorted(df["name"].tolist()))
        
        # Center coordinates
        center_lat, center_lon = 20.0, 78.0 # Default center: India/Asia
        if search_country != "-- Select --":
            match = df[df["name"] == search_country].iloc[0]
            coords = match["location_coords"]
            if coords:
                lat_str, lon_str = coords.split(",")
                center_lat, center_lon = float(lat_str), float(lon_str)
                st.success(f"Fly-to focus locked on: {search_country}")
                # Save selection for details panel
                if st.button("Open UPSC Dossier"):
                    st.session_state["selected_country_id"] = int(match["id"])
                    st.session_state["current_page"] = "Country Dossiers"
                    st.rerun()

    # Build 3D Globe
    fig = go.Figure()

    # Map selected layers to color values
    if selected_layer == "Political & Continents":
        df["val"] = df["continent"].astype("category").cat.codes
        colorscale = "Viridis"
        colorbar_title = "Continent ID"
    elif selected_layer == "Climate Zones (Köppen)":
        # Simulate value based on ID for classification coloring
        df["val"] = df["id"] % 6
        colorscale = "Rainbow"
        colorbar_title = "Climate Zone"
    elif selected_layer == "Population Density Heatmap":
        df["val"] = df["population"] / 1000000.0  # Population in Millions
        colorscale = "YlOrRd"
        colorbar_title = "Population (M)"
    else: # GDP
        df["val"] = df["gdp"]
        colorscale = "Electric"
        colorbar_title = "GDP (Billion USD)"

    # Add Choropleth boundaries layer
    fig.add_trace(go.Choropleth(
        locations=df["code"],
        z=df["val"],
        text=df["name"],
        locationmode="ISO-3",
        colorscale=colorscale,
        autocolorscale=False,
        reversescale=False,
        marker_line_color="rgba(255,255,255,0.2)",
        marker_line_width=0.6,
        colorbar=dict(
            title=dict(text=colorbar_title, font=dict(color="#f3f4f6")),
            thickness=15,
            x=0.05,
            y=0.5,
            len=0.4,
            tickcolor="#f3f4f6"
        )
    ))

    # Add capitals layer
    if show_capitals:
        cap_lats, cap_lons, cap_texts = [], [], []
        # Query details for capitals (or approximate using coordinate list)
        for _, row in df.iterrows():
            coords = row["location_coords"]
            if coords:
                lat_str, lon_str = coords.split(",")
                cap_lats.append(float(lat_str))
                cap_lons.append(float(lon_str))
                cap_texts.append(f"{row['name']}")

        fig.add_trace(go.Scattergeo(
            lon=cap_lons,
            lat=cap_lats,
            text=cap_texts,
            mode="markers",
            name="Capitals",
            marker=dict(
                size=6,
                color="#f472b6",
                line=dict(width=1, color="white")
            )
        ))

    # Add mountain peaks layer (Static Mock data overlay based on coordinate grids)
    if show_mountains:
        peak_lats = [27.9881, -32.6532, 45.8327, 35.8808, -3.0674, 43.0781]
        peak_lons = [86.9250, -70.0109, 6.8650, 76.5133, 37.3556, -118.5714]
        peak_names = ["Mt. Everest (8,848m)", "Mt. Aconcagua (6,961m)", "Mt. Blanc (4,810m)", "K2 (8,611m)", "Mt. Kilimanjaro (5,895m)", "Mt. Whitney (4,421m)"]
        
        fig.add_trace(go.Scattergeo(
            lon=peak_lons,
            lat=peak_lats,
            text=peak_names,
            mode="markers+text",
            name="Mountain Peaks",
            textposition="top center",
            marker=dict(
                size=8,
                color="#60a5fa",
                symbol="triangle-up",
                line=dict(width=1, color="white")
            )
        ))

    # Add Mineral Deposits
    if show_minerals:
        mineral_lats = [22.5, 31.5, 55.0, -29.0, 23.0]
        mineral_lons = [85.5, 45.0, 110.0, 22.0, -102.0]
        mineral_names = ["Singhbhum Iron Ore (India)", "Ghawar Petroleum (Saudi Arabia)", "Siberian Coal (Russia)", "Witwatersrand Gold (South Africa)", "Zacatecas Silver (Mexico)"]

        fig.add_trace(go.Scattergeo(
            lon=mineral_lons,
            lat=mineral_lats,
            text=mineral_names,
            mode="markers",
            name="Minerals",
            marker=dict(
                size=8,
                color="#fbbf24",
                symbol="diamond",
                line=dict(width=1, color="black")
            )
        ))

    # Setup orthographic layout with user center
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection=dict(
                type="orthographic",
                rotation=dict(lon=center_lon, lat=center_lat, roll=0)
            ),
            backgroundcolor="#0b0f19",
            lakecolor="#111827",
            landcolor="#1f2937",
            oceancolor="#0c101b",
            subunitcolor="rgba(255,255,255,0.1)",
            countrycolor="rgba(255,255,255,0.15)",
            countrywidth=0.5,
            showland=True,
            showocean=True,
            showlakes=True,
            showcountries=True
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#0b0f19",
        plot_bgcolor="#0b0f19",
        height=650,
        showlegend=True,
        legend=dict(
            x=0.85,
            y=0.1,
            bgcolor="rgba(11, 15, 25, 0.7)",
            font=dict(color="#f3f4f6")
        )
    )

    with col_globe:
        st.plotly_chart(fig, use_container_width=True)

    # Fast learning widgets at the bottom
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💡 Daily Geography Spotlight")
    st.write(
        "**Geopolitics fact:** The **Strait of Malacca** connects the Indian Ocean with the South China Sea. "
        "It is one of the world's most critical maritime chokepoints, carrying over 25% of global oil shipments daily."
    )
    st.markdown("</div>", unsafe_allow_html=True)
