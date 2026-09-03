import streamlit as st
import datetime
from frontend.api_client import make_request

def render_study_desk():
    st.markdown('<div class="gradient-header">UPSC Study Desk</div>', unsafe_allow_html=True)
    st.markdown("Revise marked facts, flashcards with SM-2 spaced repetition scheduler, and compile personal notes.")

    tab_flashcards, tab_bookmarks, tab_notes = st.tabs(["⚡ Flashcards (SM-2)", "📌 Bookmarked Facts", "📝 Saved Study Notes"])

    with tab_flashcards:
        st.markdown("### Spaced Repetition Flashcards")
        
        # Sub columns for Flashcard session vs creation
        col_session, col_create = st.columns([2, 1])

        with col_session:
            st.markdown("#### Revision Session")
            due_cards = make_request("GET", "/api/study/flashcards/due")
            
            if not due_cards:
                st.success("🎉 All caught up! No flashcards due for revision right now.")
            else:
                st.info(f"You have **{len(due_cards)}** cards due for review.")
                card = due_cards[0]
                
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(f"**Front:**\n### {card['front']}")
                
                # Check reveal answer toggle
                reveal = st.checkbox("Reveal Answer", key=f"rev_{card['id']}")
                if reveal:
                    st.markdown("---")
                    st.markdown(f"**Back:**\n{card['back']}")
                    
                    st.markdown("---")
                    st.write("Rate your recall quality:")
                    cols_rate = st.columns(6)
                    ratings = [
                        ("0: Blackout", 0),
                        ("1: Wrong", 1),
                        ("2: Hard", 2),
                        ("3: Medium", 3),
                        ("4: Good", 4),
                        ("5: Perfect", 5)
                    ]
                    for idx, (label, val) in enumerate(ratings):
                        with cols_rate[idx]:
                            if st.button(label, key=f"rate_{val}_{card['id']}"):
                                make_request("POST", "/api/study/flashcards/review", data={
                                    "card_id": int(card["id"]),
                                    "rating": val
                                })
                                st.success("SM-2 interval recalculated!")
                                st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

        with col_create:
            st.markdown("#### Create New Flashcard")
            front_text = st.text_input("Front Side (Question/Term)")
            back_text = st.text_area("Back Side (Answer/Fact)")
            if st.button("Add Flashcard"):
                if front_text and back_text:
                    res = make_request("POST", "/api/study/flashcards", data={
                        "front": front_text,
                        "back": back_text
                    })
                    if res:
                        st.success("New flashcard created!")
                        st.rerun()
                else:
                    st.warning("Please fill both front and back fields.")

    with tab_bookmarks:
        st.markdown("### Bookmarked Facts Database")
        bookmarks = make_request("GET", "/api/study/bookmarks")
        
        if not bookmarks:
            st.info("You haven't bookmarked any geography facts yet. Add bookmarks inside country dossiers!")
        else:
            for b in bookmarks:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                col_b1, col_b2 = st.columns([3, 1])
                with col_b1:
                    st.markdown(f"**Country:** {b['country_name']} | **Section:** `{b['section']}`")
                    st.markdown(f"**{b['fact_key']}**: {b['fact_value']}")
                with col_b2:
                    if st.button("Delete Bookmark", key=f"del_b_{b['id']}"):
                        make_request("DELETE", f"/api/study/bookmarks/{b['id']}")
                        st.success("Deleted!")
                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

    with tab_notes:
        st.markdown("### Compiled Study Dossiers & Notes")
        notes = make_request("GET", "/api/study/notes")
        
        if not notes:
            st.info("No personal notes found. Access Country Dossiers to write and save notes!")
        else:
            for n in notes:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(f"### {n['country_name']} Notes")
                st.markdown(f"*Last updated: {n['updated_at']}*")
                st.markdown(n["note_content"])
                st.markdown("</div>", unsafe_allow_html=True)
