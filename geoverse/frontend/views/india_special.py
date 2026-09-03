import streamlit as st
import json
from frontend.api_client import make_request

def render_india_special():
    st.markdown('<div class="gradient-header">India Special Geography Module</div>', unsafe_allow_html=True)
    st.markdown("Granular physical, demographic, and infrastructure dossiers covering all 28 States and 8 Union Territories.")

    tab_states, tab_disputes, tab_regions = st.tabs(["🇮🇳 State/UT Dossier", "💧 Water Disputes", "🏔️ Geographical Regions"])

    # Fetch states data
    states = make_request("GET", "/api/india/states")

    with tab_states:
        if not states:
            st.info("Loading India data. Run seeder to populate State databases.")
        else:
            state_names = sorted([s["name"] for s in states])
            selected_state_name = st.selectbox("Select State or UT Profile:", state_names)
            
            s = next(state for state in states if state["name"] == selected_state_name)
            
            st.markdown(f"## {s['name']} Dossier (`{s['type']}`)")
            st.write(f"**Administrative Capital:** {s['capital']}")
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 🌋 Geomorphic Features")
                st.write("**Rivers:**")
                rivers = json.loads(s.get("rivers_json") or "[]")
                for r in rivers:
                    st.write(f"- {r.get('name')} (Length: {r.get('length')} km)")
                st.write("**Mountains/Ridges:**")
                mountains = json.loads(s.get("mountains_json") or "[]")
                for m in mountains:
                    st.write(f"- {m.get('name')} (Peak elevation: {m.get('elevation')} m)")
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 🌱 Soils & Crop Systems")
                soils = json.loads(s.get("soils_json") or "[]")
                st.write(f"**Soils:** {', '.join(soils)}")
                crops = json.loads(s.get("crops_json") or "[]")
                st.write(f"**Crops:** {', '.join(crops)}")
                st.markdown("</div>", unsafe_allow_html=True)

            with col_d2:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 💎 Mineral deposits & Industries")
                minerals = json.loads(s.get("minerals_json") or "[]")
                st.write(f"**Minerals:** {', '.join(minerals)}")
                industries = json.loads(s.get("industries_json") or "[]")
                st.write(f"**Major Industries:** {', '.join(industries)}")
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 🛣️ Dams & Transport Infrastructure")
                dams = json.loads(s.get("dams_json") or "[]")
                for dam in dams:
                    st.write(f"- {dam.get('name')} (Power capacity: {dam.get('capacity')})")
                highways = json.loads(s.get("highways_json") or "[]")
                st.write(f"**National Highways:** {', '.join(highways)}")
                st.markdown("</div>", unsafe_allow_html=True)

            # Special/Tribal Areas Info
            tribal = json.loads(s.get("tribal_areas_json") or "[]")
            if tribal:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 👥 Scheduled & Tribal Demography")
                for t in tribal:
                    st.write(f"- {t}")
                st.markdown("</div>", unsafe_allow_html=True)

    with tab_disputes:
        st.markdown("### Interstate Water Sharing & River Disputes")
        
        disputes = [
            {"river": "Cauvery River", "states": "Karnataka, Tamil Nadu, Kerala, Puducherry", "issue": "Historical water sharing agreement allocation. Karnataka opposes water release mandates during low rainfall monsoon deficit years.", "tribunal": "Cauvery Water Disputes Tribunal (CWDT) & Cauvery Water Management Authority (CWMA)"},
            {"river": "Krishna River", "states": "Maharashtra, Karnataka, Andhra Pradesh, Telangana", "issue": "Allocation of water based on surplus estimates. Telangana disputes legacy Andhra Pradesh division ratios.", "tribunal": "Krishna Water Disputes Tribunal (KWDT II)"},
            {"river": "Mahanadi River", "states": "Chhattisgarh, Odisha", "issue": "Odisha objects to Chhattisgarh constructing barrages upstream, limiting seasonal dry-season flows.", "tribunal": "Mahanadi Water Disputes Tribunal (formed 2018)"},
            {"river": "Sutlej-Yamuna Link (SYL) Canal", "states": "Punjab, Haryana", "issue": "Construction of canal link to share Ravi-Beas waters. Punjab claims water scarcity prevents sharing; Haryana demands immediate completion.", "tribunal": "Supreme Court directed mandates"}
        ]

        for disp in disputes:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"#### 💧 {disp['river']} Dispute")
            st.write(f"**Involved Entities:** *{disp['states']}*")
            st.write(f"**Core Issue:** {disp['issue']}")
            st.write(f"**Status / Authority:** *{disp['tribunal']}*")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_regions:
        st.markdown("### India's Macro Physiographic Regions")
        
        regions = {
            "Himalayan Northern Mountains": {
                "extent": "Pamir knot to Northeast frontier. Length ~2400 km.",
                "subdivisions": "Trans-Himalayas (Karakoram, Ladakh, Zaskar), Great Himalayas (Himadri), Lesser Himalayas (Himachal), Outer Himalayas (Shiwaliks).",
                "importance": "Climatic barrier shielding plains from cold Siberian winds, source of perennial rivers, rich forest biodiversity."
            },
            "Great Indo-Gangetic Plains": {
                "extent": "Depression between Himalayas and Peninsula filled with alluvial sediments.",
                "subdivisions": "Bhabar (porous gravel), Tarai (marshy wet), Bhangar (older clayey alluvium), Khadar (newer fertile silt).",
                "importance": "High-density crop production zone (Wheat/Rice belt), groundwater reservoir."
            },
            "Peninsular Deccan Plateau": {
                "extent": "Triangular landmass south of Vindhyas. Stable ancient shield.",
                "subdivisions": "Central Highlands (Malwa, Bundelkhand), Deccan Trap (Lava basalt), Eastern Plateau (Chhota Nagpur).",
                "importance": "Storehouse of Indian minerals (iron, coal, bauxite, manganese). High black regur cotton soils."
            },
            "Thar Arid Desert": {
                "extent": "West of Aravalli range in Rajasthan.",
                "subdivisions": "Marusthali (sand dune sheets) and Semi-desert bagar plains.",
                "importance": "Solar and wind energy potential, unique sand saline lakes (Sambhar Lake salt production)."
            }
        }

        for name, details in regions.items():
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"### 🏔️ {name}")
            st.write(f"**Physical Extent:** {details['extent']}")
            st.write(f"**Physiographic Subdivisions:** {details['subdivisions']}")
            st.write(f"**Strategic & Economic Importance:** {details['importance']}")
            st.markdown("</div>", unsafe_allow_html=True)
