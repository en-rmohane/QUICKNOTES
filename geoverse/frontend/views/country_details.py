import streamlit as st
import json
import io
from frontend.api_client import make_request
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def render_country_details():
    st.markdown('<div class="gradient-header">UPSC Country Dossier Desk</div>', unsafe_allow_html=True)
    st.markdown("Access highly granular, UPSC-syllabus oriented geographical and economic databases for key global entities.")

    # Get country lists for selection
    countries = make_request("GET", "/api/countries")
    if not countries:
        st.info("No country records found. Please run seeder.")
        return

    country_names = sorted([c["name"] for c in countries])
    
    # Check if there is a pre-selected country in session state
    default_index = 0
    if "selected_country_id" in st.session_state and st.session_state["selected_country_id"]:
        for idx, c in enumerate(countries):
            if c["id"] == st.session_state["selected_country_id"]:
                default_index = country_names.index(c["name"])
                break

    selected_country_name = st.selectbox("Select Country Dossier", country_names, index=default_index)
    
    # Fetch full country detail
    matched_country = next(c for c in countries if c["name"] == selected_country_name)
    c_id = matched_country["id"]
    st.session_state["selected_country_id"] = c_id # save in state

    detail = make_request("GET", f"/api/countries/{c_id}")
    if not detail:
        st.error("Failed to load country dossier details.")
        return

    # Check study progress
    progress_records = make_request("GET", "/api/progress")
    completed_sections = []
    if progress_records:
        for p in progress_records:
            if p["country_id"] == c_id:
                completed_sections = json.loads(p["topics_completed_json"])

    # UI columns: Left = Data & Tabs, Right = Actions, Notes & PDF
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown(f"## {detail['name']} Dossier (`{detail['code']}`)")
        
        # Summary KPI cards
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.metric("Continent", detail["continent"])
        with col_s2:
            st.metric("Population", f"{detail['population']:,}" if detail['population'] else "N/A")
        with col_s3:
            st.metric("GDP (Billion USD)", f"${detail['gdp']:.1f}" if detail['gdp'] else "N/A")
        with col_s4:
            st.metric("HDI Rank/Value", f"{detail['hdi']:.3f}" if detail['hdi'] else "N/A")

        # Organize tabs
        tab_physical, tab_climate, tab_agriculture, tab_minerals, tab_demography, tab_political, tab_special = st.tabs([
            "🌋 Physical", "🌦️ Climate", "🌱 Agriculture", "💎 Minerals & Ind", "👥 Demography", "💼 Politico-Econ", "🌟 Special"
        ])

        with tab_physical:
            st.markdown("### A. Physical Geography & Geomorphology")
            st.write(f"**Location & Extent:** {detail.get('location_coords', 'N/A')} | **Area:** {detail.get('area_sq_km', 'N/A')} sq.km")
            st.write(f"**Territorial Boundaries:** {detail.get('boundaries', 'N/A')}")
            
            # Mountain Ranges
            st.markdown("**Major Mountain Ranges:**")
            mountains = json.loads(detail.get("mountains_json") or "[]")
            for m in mountains:
                st.markdown(f"- **{m.get('name')}**: Peaks: {', '.join(m.get('peaks', []))}. *Significance:* {m.get('significance')}")

            # Peaks
            st.markdown("**Important Peaks:**")
            peaks = json.loads(detail.get("peaks_json") or "[]")
            for p in peaks:
                st.markdown(f"- **{p.get('name')}** ({p.get('height')}m) in range *{p.get('range')}*. *Note:* {p.get('significance')}")

            # Rivers
            st.markdown("**Major River Systems:**")
            rivers = json.loads(detail.get("rivers_json") or "[]")
            for r in rivers:
                st.markdown(f"- **{r.get('name')}** (Length: {r.get('length')}km) | *Origin:* {r.get('origin')} ➔ *Mouth:* {r.get('mouth')}. Tributaries: {', '.join(r.get('tributaries', []))}")

            # Lakes, Deserts, Coastlines
            col_ph1, col_ph2 = st.columns(2)
            with col_ph1:
                st.markdown("**Lakes & Deserts:**")
                lakes = json.loads(detail.get("lakes_json") or "[]")
                for l in lakes:
                    st.markdown(f"- *Lake:* **{l.get('name')}** ({l.get('type')}) - {l.get('significance')}")
                deserts = json.loads(detail.get("deserts_json") or "[]")
                for d in deserts:
                    st.markdown(f"- *Desert:* **{d.get('name')}** ({d.get('area')} sq.km) - {d.get('climate')}")
            with col_ph2:
                st.markdown("**Straits & Coastlines:**")
                straits = json.loads(detail.get("straits_json") or "[]")
                for s in straits:
                    st.markdown(f"- *Strait:* **{s.get('name')}** connects *{s.get('connects')}* - {s.get('significance')}")

        with tab_climate:
            st.markdown("### B. Climate, Hydrology & Environment")
            st.info(f"**Köppen Climate Classification:** {detail.get('koppen_classification', 'N/A')}")
            st.write(f"**Temperature Ranges:** {detail.get('temperature_avg_json', 'N/A')}")
            st.write(f"**Rainfall Patterns:** {detail.get('rainfall_json', 'N/A')}")
            st.write(f"**Wind Currents:** {detail.get('winds_json', 'N/A')}")
            
            col_cl1, col_cl2 = st.columns(2)
            with col_cl1:
                st.markdown("**Vegetation & Biospheres:**")
                veg = json.loads(detail.get("vegetation_json") or "[]")
                st.write(", ".join(veg))
                parks = json.loads(detail.get("parks_json") or "[]")
                for p in parks:
                    st.markdown(f"- {p}")
            with col_cl2:
                st.markdown("**Environmental Hazards & Disasters:**")
                st.write(f"*Issues:* {detail.get('environmental_issues', 'N/A')}")
                disasters = json.loads(detail.get("disasters_json") or "[]")
                st.write(f"*Disaster Profile:* {', '.join(disasters)}")

        with tab_agriculture:
            st.markdown("### C. Soil Pedology & Agricultural Geography")
            soils = json.loads(detail.get("soil_types_json") or "[]")
            st.markdown("**Soil Typology:**")
            for s in soils:
                st.markdown(f"- **{s.get('type')}**: Fertility is *{s.get('fertility')}* - distributed in *{s.get('distribution')}*")

            crops = json.loads(detail.get("crops_json") or "{}")
            st.write(f"**Food Crops:** {', '.join(crops.get('food_crops', []))} | **Cash Crops:** {', '.join(crops.get('cash_crops', []))}")
            st.write(f"**Farming Patterns:** {detail.get('farming_patterns', 'N/A')}")
            st.write(f"**Irrigation Networks:** {detail.get('irrigation_json', 'N/A')}")
            st.write(f"**Green Revolution Impact:** {detail.get('green_rev_impact', 'N/A')}")
            
            gi_tags = json.loads(detail.get("gi_tags_json") or "[]")
            if gi_tags:
                st.markdown(f"**Famous GI Tags:** {', '.join(gi_tags)}")

        with tab_minerals:
            st.markdown("### D. Mineral Resources & Industrial Geography")
            minerals = json.loads(detail.get("minerals_json") or "[]")
            st.markdown("**Mineral Deposits:**")
            for m in minerals:
                st.markdown(f"- **{m.get('name')}**: Grades: {m.get('grade', 'N/A')}. Deposits: {', '.join(m.get('deposits', []))}")

            mining = json.loads(detail.get("mining_regions_json") or "[]")
            st.markdown("**Mining Regions:**")
            for mr in mining:
                st.markdown(f"- **{mr.get('name')}** - Min: *{mr.get('mineral')}* (Rank: {mr.get('production_rank')})")

            st.write(f"**Industrial Corridors:** {detail.get('corridors_json', 'N/A')}")
            st.write(f"**Energy Resources:** {detail.get('energy_resources_json', 'N/A')}")
            st.write(f"**Refineries & Pipelines:** {detail.get('pipelines_refineries_json', 'N/A')}")

        with tab_demography:
            st.markdown("### E. Population Geography & Demography")
            st.write(f"**Total Population:** {detail.get('population')} | **Density:** {detail.get('density')} per sq.km")
            st.write(f"**Growth Rate:** {detail.get('growth_rate')}% | **Urbanization Rate:** {detail.get('urbanization_rate')}%")
            st.write(f"**Literacy Rate:** {detail.get('literacy_rate')}% | **Sex Ratio:** {detail.get('sex_ratio')}")
            
            st.markdown("**Major Cities & Industrial Hubs:**")
            cities = json.loads(detail.get("cities_json") or "[]")
            for city in cities:
                st.markdown(f"- **{city.get('name')}** (Pop: {city.get('population'):,}) - *Significance:* {city.get('significance')}")

        with tab_political:
            st.markdown("### F. Political & Economic Infrastructure")
            st.write(f"**Government Type:** {detail.get('government_type')} | **Currency:** {detail.get('currency')}")
            st.write(f"**GDP:** ${detail.get('gdp')} Billion | **GDP per Capita:** ${detail.get('gdp_per_capita'):.2f}")
            
            trade = json.loads(detail.get("trade_json") or "{}")
            if trade:
                st.write(f"**Exports:** {', '.join(trade.get('exports', []))} | **Imports:** {', '.join(trade.get('imports', []))}")
                st.write(f"**Trade Partners:** {', '.join(trade.get('partners', []))}")

            st.markdown("**Transportation Infrastructure:**")
            st.write(f"*Sea Ports:* {', '.join(json.loads(detail.get('ports_json') or '[]'))}")
            st.write(f"*Air Hubs:* {', '.join(json.loads(detail.get('airports_json') or '[]'))}")

        with tab_special:
            st.markdown("### G. Geopolitics & Special Features")
            st.write(f"**Geopolitical Choke Points / Strategic Significance:** {detail.get('geopolitical_significance', 'N/A')}")
            st.write(f"**Boundaries & Disputes:** {detail.get('border_disputes_json', 'N/A')}")
            
            treaties = json.loads(detail.get("treaties_json") or "[]")
            st.markdown(f"**International Treaties:** {', '.join(treaties)}")
            st.write(f"**Bilateral/Regional Relations:** {detail.get('relations_json', 'N/A')}")

    with col_right:
        st.markdown("### 📝 Study Companion")
        
        # Section progress update checkboxes
        st.markdown("**Section Study Tracker:**")
        sections = ["Physical", "Climate", "Agriculture", "Minerals", "Demography", "Political", "Special"]
        for sec in sections:
            checked = sec in completed_sections
            box = st.checkbox(f"Completed {sec}", value=checked, key=f"check_prog_{sec}_{c_id}")
            if box != checked:
                # API Call to update progress
                make_request("POST", "/api/progress", data={"country_id": int(c_id), "section": sec})
                st.success(f"Progress saved for {sec}!")
                st.rerun()

        # Add Bookmark
        st.markdown("---")
        st.markdown("**Quick Bookmark Fact:**")
        bookmark_sec = st.selectbox("Topic Section", sections, key="b_sec")
        b_key = st.text_input("Fact Keyword (e.g. Major Peak)", key="b_key")
        b_val = st.text_input("Fact Detail (e.g. Kanchenjunga 8586m)", key="b_val")
        if st.button("Bookmark Fact"):
            if b_key and b_val:
                make_request("POST", "/api/study/bookmarks", data={
                    "country_id": int(c_id),
                    "section": bookmark_sec,
                    "fact_key": b_key,
                    "fact_value": b_val
                })
                st.success("Fact bookmarked successfully!")
            else:
                st.warning("Please fill keyword and detail.")

        # Rich text notes block
        st.markdown("---")
        st.markdown("**Personal Study Notes (Markdown Support):**")
        notes_data = make_request("GET", "/api/study/notes")
        existing_note = ""
        if notes_data:
            for n in notes_data:
                if n["country_id"] == c_id:
                    existing_note = n["note_content"]
                    break

        user_note_text = st.text_area("Write notes/reminders for this country:", value=existing_note, height=200, key="notes_area")
        if st.button("Save Notes"):
            make_request("POST", "/api/study/notes", data={
                "country_id": int(c_id),
                "note_content": user_note_text
            })
            st.success("Study notes updated!")

        # PDF Export button
        st.markdown("---")
        st.markdown("**Document Exporter:**")
        if st.button("Generate PDF Dossier"):
            pdf_bytes = generate_country_pdf(detail)
            st.download_button(
                label="📥 Download PDF fact sheet",
                data=pdf_bytes,
                file_name=f"{detail['name']}_UPSC_Geography_Dossier.pdf",
                mime="application/pdf"
            )

def generate_country_pdf(detail):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=colors.HexColor('#1e3a8a'),
        spaceAfter=15
    )
    h2_style = ParagraphStyle(
        'H2Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=colors.HexColor('#2563eb'),
        spaceBefore=10,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        spaceAfter=8
    )

    # Document Title
    story.append(Paragraph(f"{detail['name']} - UPSC Geography Dossier", title_style))
    story.append(Paragraph(f"Continent: {detail['continent']} | Population: {detail.get('population', 'N/A')} | GDP: {detail.get('gdp', 'N/A')} Billion USD", body_style))
    story.append(Spacer(1, 10))

    # General Info
    story.append(Paragraph("A. Physical Geography", h2_style))
    story.append(Paragraph(f"<b>Location coords:</b> {detail.get('location_coords', 'N/A')}", body_style))
    story.append(Paragraph(f"<b>Boundaries:</b> {detail.get('boundaries', 'N/A')}", body_style))
    story.append(Paragraph(f"<b>Mountains:</b> {detail.get('mountains_json', '[]')}", body_style))
    story.append(Paragraph(f"<b>Rivers:</b> {detail.get('rivers_json', '[]')}", body_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("B. Climate & Environment", h2_style))
    story.append(Paragraph(f"<b>Koppen classification:</b> {detail.get('koppen_classification', 'N/A')}", body_style))
    story.append(Paragraph(f"<b>Environmental Issues:</b> {detail.get('environmental_issues', 'N/A')}", body_style))
    story.append(Paragraph(f"<b>Hazards/Disasters:</b> {detail.get('disasters_json', '[]')}", body_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("C. Minerals & Resource Profile", h2_style))
    story.append(Paragraph(f"<b>Minerals:</b> {detail.get('minerals_json', '[]')}", body_style))
    story.append(Paragraph(f"<b>Mining Regions:</b> {detail.get('mining_regions_json', '[]')}", body_style))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
