import streamlit as st
import pandas as pd
import plotly.express as px
from frontend.api_client import make_request

def render_compare_mode():
    st.markdown('<div class="gradient-header">Country Comparison Deck</div>', unsafe_allow_html=True)
    st.markdown("Compare critical UPSC geography parameters across multiple countries side-by-side.")

    # Get country lists for selection
    countries = make_request("GET", "/api/countries")
    if not countries:
        st.info("No country records found. Please run seeder.")
        return

    country_names = sorted([c["name"] for c in countries])
    
    # Multiselect for countries (limited to 3)
    selected_names = st.multiselect(
        "Select up to 3 countries to compare:",
        country_names,
        default=country_names[:2] if len(country_names) >= 2 else country_names
    )

    if not selected_names:
        st.warning("Please select at least one country to begin comparison.")
        return

    if len(selected_names) > 3:
        st.error("You can select a maximum of 3 countries at a time.")
        return

    # Fetch details for selected countries
    selected_details = []
    for name in selected_names:
        matched = next(c for c in countries if c["name"] == name)
        detail = make_request("GET", f"/api/countries/{matched['id']}")
        if detail:
            selected_details.append(detail)

    if not selected_details:
        st.error("Failed to load country profiles.")
        return

    # Create comparison table columns
    st.markdown("### 📊 Parameter Comparison Grid")
    
    comp_data = {
        "Metric / Parameter": [
            "Continent",
            "Coordinates",
            "Area (sq km)",
            "Population",
            "Population Density (/sq km)",
            "HDI Value",
            "Köppen Climate Type",
            "Government",
            "Currency",
            "GDP (Billion USD)",
            "GDP per Capita (USD)",
            "Literacy Rate (%)",
            "Sex Ratio",
            "Time Zone(s)"
        ]
    }

    for c in selected_details:
        comp_data[c["name"]] = [
            c.get("continent"),
            c.get("location_coords"),
            f"{c.get('area_sq_km', 0):,}" if c.get('area_sq_km') else "N/A",
            f"{c.get('population', 0):,}" if c.get('population') else "N/A",
            f"{c.get('density', 0):.2f}" if c.get('density') else "N/A",
            f"{c.get('hdi', 0):.3f}" if c.get('hdi') else "N/A",
            c.get("koppen_classification"),
            c.get("government_type"),
            c.get("currency"),
            f"${c.get('gdp', 0):.1f}" if c.get('gdp') else "N/A",
            f"${c.get('gdp_per_capita', 0):,.2f}" if c.get('gdp_per_capita') else "N/A",
            f"{c.get('literacy_rate', 0):.1f}%" if c.get('literacy_rate') else "N/A",
            c.get("sex_ratio"),
            c.get("timezones_json") or "N/A"
        ]

    df_comp = pd.DataFrame(comp_data)
    st.dataframe(df_comp, use_container_width=True, hide_index=True)

    # Graphical Comparisons
    st.markdown("### 📈 Visual Analytics Charts")
    
    col_chart1, col_chart2 = st.columns(2)
    
    # Prepare comparison dataframe for charting
    chart_rows = []
    for c in selected_details:
        chart_rows.append({
            "Country": c["name"],
            "GDP (Billion $)": c.get("gdp") or 0,
            "Population (Millions)": (c.get("population") or 0) / 1000000.0,
            "HDI Score": c.get("hdi") or 0.0,
            "Literacy (%)": c.get("literacy_rate") or 0.0
        })
    df_chart = pd.DataFrame(chart_rows)

    with col_chart1:
        st.write("**GDP Comparison (Billion USD)**")
        fig_gdp = px.bar(
            df_chart, 
            x="Country", 
            y="GDP (Billion $)", 
            color="Country",
            text="GDP (Billion $)",
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_gdp.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False
        )
        st.plotly_chart(fig_gdp, use_container_width=True)

    with col_chart2:
        st.write("**Population Comparison (Millions)**")
        fig_pop = px.bar(
            df_chart, 
            x="Country", 
            y="Population (Millions)", 
            color="Country",
            text="Population (Millions)",
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_pop.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False
        )
        st.plotly_chart(fig_pop, use_container_width=True)

    # Detailed comparative note box
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📝 comparative UPSC study prompt")
    
    if len(selected_details) >= 2:
        c1, c2 = selected_details[0], selected_details[1]
        st.write(
            f"**Key observations for analysis:** Notice the differences in economic intensity: "
            f"*{c1['name']}* has a GDP of **${c1.get('gdp')}B** with an HDI of **{c1.get('hdi')}**, while "
            f"*{c2['name']}* has **${c2.get('gdp')}B** with an HDI of **{c2.get('hdi')}**.\n\n"
            f"Check the agricultural and mineral alignment between them. Climate classification shows "
            f"*{c1['name']}* is characterized by *{c1.get('koppen_classification')}* zones compared to *{c2['name']}*'s *{c2.get('koppen_classification')}* zones. "
            f"This dictates crop cultivation patterns and water resource management policies."
        )
    st.markdown("</div>", unsafe_allow_html=True)
