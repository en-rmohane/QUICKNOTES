import streamlit as st
import folium
from streamlit_folium import folium_static
from frontend.api_client import make_request

def render_current_affairs():
    st.markdown('<div class="gradient-header">Geography & Environmental Current Affairs</div>', unsafe_allow_html=True)
    st.markdown("Track disaster events, volcanic eruptions, and infrastructural updates mapped globally.")

    # Fetch news tracker feed
    news_list = make_request("GET", "/api/news")

    if not news_list:
        st.info("No mapped events found. Events will appear here as they are added via the admin panel.")
        return

    # Create Folium Map centered on middle latitudes
    m = folium.Map(location=[20, 30], zoom_start=2, tiles="cartodbpositron")

    # Categories to colors
    cat_colors = {
        "Disaster": "red",
        "Infrastructure": "blue",
        "Climate": "green",
        "Geopolitics": "purple"
    }

    # Add markers for news items with valid coordinates
    for n in news_list:
        coords_str = n.get("coordinates_json")
        if coords_str:
            try:
                lat_str, lon_str = coords_str.split(",")
                lat, lon = float(lat_str), float(lon_str)
                
                # HTML popup card
                popup_html = f"""
                <div style="font-family: 'Inter', sans-serif; width: 220px;">
                    <h4 style="margin: 0 0 5px; color: #1e3a8a;">{n['title']}</h4>
                    <span style="font-size: 0.8rem; background: #e5e7eb; padding: 2px 6px; border-radius: 4px; font-weight: 500;">{n['category']}</span>
                    <p style="font-size: 0.85rem; color: #374151; margin-top: 5px;">{n['summary']}</p>
                </div>
                """
                
                folium.Marker(
                    location=[lat, lon],
                    popup=folium.Popup(popup_html, max_width=250),
                    tooltip=n["title"],
                    icon=folium.Icon(color=cat_colors.get(n["category"], "gray"), icon="info-sign")
                ).add_to(m)
            except Exception as e:
                pass

    # Layout: Map on top, news articles list below
    col_map, col_list = st.columns([2, 1])

    with col_map:
        st.markdown("### 🗺️ Live Event Map")
        folium_static(m)

    with col_list:
        st.markdown("### 📰 Latest Bulletins")
        for n in news_list:
            st.markdown(f'<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"**[{n['category']}]** | *{n['date_published'][:10]}*")
            st.markdown(f"#### {n['title']}")
            st.write(n["summary"])
            if n.get("url"):
                st.markdown(f"[Read Source Bulletin]({n['url']})")
            st.markdown("</div>", unsafe_allow_html=True)
