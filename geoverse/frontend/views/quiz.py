import streamlit as st
import json
import time
from frontend.api_client import make_request

def render_quiz_engine():
    st.markdown('<div class="gradient-header">UPSC Geography Quiz Arena</div>', unsafe_allow_html=True)
    st.markdown("Practice high-yield Assertion-Reason, Matching, and Previous Year Questions (2010-2024).")

    # Initialize quiz state variables
    if "quiz_questions" not in st.session_state:
        st.session_state["quiz_questions"] = []
        st.session_state["current_question_index"] = 0
        st.session_state["quiz_score"] = 0
        st.session_state["quiz_answers"] = {}
        st.session_state["quiz_active"] = False
        st.session_state["start_time"] = 0
        st.session_state["time_limit"] = 0

    # User overall statistics block
    stats = make_request("GET", "/api/quizzes/stats")
    
    col_stat1, col_stat2 = st.columns([1, 2])
    with col_stat1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🏆 Performance Card")
        if stats:
            st.metric("Total Questions Answered", stats.get("total_attempts", 0))
            st.metric("Accuracy Rate", f"{stats.get('accuracy', 0.0):.1f}%")
        else:
            st.write("No stats recorded yet. Complete a quiz!")
        if "user" in st.session_state and st.session_state["user"]:
            st.metric("Total Experience XP", f"{st.session_state['user'].get('xp', 0)} XP")
            st.metric("Login Study Streak", f"🔥 {st.session_state['user'].get('streak', 0)} Days")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_stat2:
        if not st.session_state["quiz_active"]:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### ⚙️ Configure Custom Mock Test")
            
            topic = st.selectbox(
                "Select Focus Topic", 
                ["All", "Physical Geography", "Political Geography", "Climatology", "Soil & Agriculture", "Economic Geography", "India Special"]
            )
            difficulty = st.selectbox(
                "Select Difficulty Level", 
                ["All", "Easy", "Medium", "Hard", "UPSC_Level"]
            )
            limit = st.slider("Number of Questions", 5, 20, 10)
            
            if st.button("🚀 Start Timed Mock Challenge"):
                # Fetch questions from API
                api_topic = None if topic == "All" else topic
                api_diff = None if difficulty == "All" else difficulty
                
                questions = make_request(
                    "GET", 
                    "/api/quizzes/random", 
                    params={"topic": api_topic, "difficulty": api_diff, "limit": limit}
                )
                
                if questions:
                    st.session_state["quiz_questions"] = questions
                    st.session_state["current_question_index"] = 0
                    st.session_state["quiz_score"] = 0
                    st.session_state["quiz_answers"] = {}
                    st.session_state["quiz_active"] = True
                    st.session_state["start_time"] = time.time()
                    st.session_state["time_limit"] = limit * 60 # 1 minute per question
                    st.rerun()
                else:
                    st.error("No questions found matching your filter criteria. Try expanding topics/difficulty.")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            # Quiz is active
            questions = st.session_state["quiz_questions"]
            idx = st.session_state["current_question_index"]
            total_q = len(questions)

            # Timer
            elapsed = time.time() - st.session_state["start_time"]
            remaining = max(0, st.session_state["time_limit"] - int(elapsed))
            mins, secs = divmod(remaining, 60)
            
            st.markdown(f"**Question {idx + 1} of {total_q}** | ⏳ Time Remaining: **{mins:02d}:{secs:02d}**")
            
            # Progress bar
            st.progress((idx) / total_q)
            
            if remaining <= 0:
                st.error("⏳ Time is up!")
                st.session_state["quiz_active"] = False
                st.rerun()

            q = questions[idx]
            
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.write(f"**[{q['topic']} | {q['difficulty']}]**")
            st.markdown(f"### {q['question_text']}")
            
            options = json.loads(q["options_json"])
            
            # Selection
            selected_option = st.radio("Choose the correct option:", options, key=f"q_radio_{idx}")
            
            col_nav1, col_nav2 = st.columns(2)
            with col_nav2:
                if st.button("Submit Answer ➡️"):
                    selected_index = str(options.index(selected_option))
                    
                    # Submit to API
                    res = make_request("POST", "/api/quizzes/submit", data={
                        "quiz_id": int(q["id"]),
                        "selected_answer": selected_index,
                        "time_taken": int(elapsed / total_q) # approximate time per question
                    })
                    
                    st.session_state["quiz_answers"][idx] = {
                        "question": q["question_text"],
                        "selected": selected_option,
                        "correct": options[int(res["correct_answer"])],
                        "is_correct": res["is_correct"],
                        "explanation": res["explanation"]
                    }
                    
                    if res["is_correct"]:
                        st.session_state["quiz_score"] += 1
                        st.balloons()
                    
                    # Navigate to next or end
                    if idx + 1 < total_q:
                        st.session_state["current_question_index"] += 1
                    else:
                        st.session_state["quiz_active"] = False
                        # Update user profile in session to refresh XP
                        profile = make_request("GET", "/api/auth/me")
                        if profile:
                            st.session_state["user"] = profile
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # Show review of last completed quiz
    if not st.session_state["quiz_active"] and st.session_state["quiz_answers"]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("## 🏁 Quiz Scorecard Summary")
        score = st.session_state["quiz_score"]
        total = len(st.session_state["quiz_questions"])
        pct = (score / total * 100) if total > 0 else 0
        
        st.success(f"You scored **{score}/{total}** ({pct:.1f}%)")
        
        # Detailed review
        for idx, item in st.session_state["quiz_answers"].items():
            color = "green" if item["is_correct"] else "red"
            mark = "✅" if item["is_correct"] else "❌"
            st.markdown(f"**Q{idx + 1}: {item['question']}**")
            st.markdown(f"Your answer: <span style='color:{color}'>{mark} {item['selected']}</span>", unsafe_allow_html=True)
            if not item["is_correct"]:
                st.markdown(f"Correct answer: **{item['correct']}**")
            st.info(f"**Explanation:** {item['explanation']}")
            st.markdown("---")
            
        if st.button("Clear Scorecard"):
            st.session_state["quiz_answers"] = {}
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
