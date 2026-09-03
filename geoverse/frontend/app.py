import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from frontend.api_client import make_request, login, register, logout

# Page Config
st.set_page_config(
    page_title="GeoVerse: 3D Interactive Geography Learning Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling Load Helper
def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found at {file_path}")

# Load custom styling
css_path = os.path.join(os.path.dirname(__file__), "styles", "custom.css")
load_css(css_path)

# Initialize Session State
if "token" not in st.session_state:
    st.session_state["token"] = None
if "user" not in st.session_state:
    st.session_state["user"] = None
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "3D Globe View"
if "selected_country_id" not in st.session_state:
    st.session_state["selected_country_id"] = None

# --- AUTHENTICATION SHIELD ---
if not st.session_state["token"] or not st.session_state["user"]:
    st.markdown('<div class="gradient-header" style="text-align:center;">Welcome to GeoVerse</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.2rem; color:#9ca3af;'>Interactive 3D Geography Learning Platform tailored for General Geography and UPSC Aspirants</p>", unsafe_allow_html=True)
    
    col_login, col_reg = st.columns(2)
    
    with col_login:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🔑 Student / Admin Sign In")
        l_user = st.text_input("Username", key="l_user")
        l_pass = st.text_input("Password", type="password", key="l_pass")
        if st.button("Sign In", key="btn_signin"):
            if login(l_user, l_pass):
                st.success("Successfully logged in!")
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_reg:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Register New Account")
        r_user = st.text_input("Choose Username", key="r_user")
        r_email = st.text_input("Email Address", key="r_email")
        r_pass = st.text_input("Choose Password", type="password", key="r_pass")
        if st.button("Sign Up", key="btn_signup"):
            if r_user and r_email and r_pass:
                res = register(r_user, r_email, r_pass)
                if res:
                    st.success("Account registered successfully! You can now sign in.")
            else:
                st.warning("Please fill all signup fields.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    # Quick demo account hint
    st.markdown(
        "<p style='text-align:center; color:#9ca3af; font-size:0.9rem; margin-top:20px;'>"
        "💡 Hint: You can use the seeded Administrator account (Username: <code>admin</code>, Password: <code>admin123</code>)"
        "</p>", 
        unsafe_allow_html=True
    )
    st.stop()

# --- MAIN LOGGED-IN PORTAL ---

# Import page rendering engines dynamically to avoid circular issues
from frontend.views.globe_view import render_globe_view
from frontend.views.country_details import render_country_details
from frontend.views.compare import render_compare_mode
from frontend.views.india_special import render_india_special
from frontend.views.quiz import render_quiz_engine
from frontend.views.study_desk import render_study_desk
from frontend.views.current_affairs import render_current_affairs
from frontend.views.admin import render_admin_panel

# Sidebar Navigation Panel
st.sidebar.markdown('<div style="padding:10px 0;"><h2 style="color:#60a5fa; margin:0;">🌍 GeoVerse Portal</h2></div>', unsafe_allow_html=True)

# User Info card in sidebar
u = st.session_state["user"]
st.sidebar.markdown(
    f'<div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:8px; border:1px solid rgba(255,255,255,0.08); margin-bottom:20px;">'
    f'  <p style="margin:0; font-size:0.8rem; color:#9ca3af;">AUTHENTICATED USER</p>'
    f'  <h4 style="margin:2px 0; color:#f3f4f6;">👤 {u["username"]}</h4>'
    f'  <p style="margin:0; font-size:0.9rem; color:#a78bfa;">🔥 Streak: <b>{u.get("streak", 0)} days</b> | 🏆 <b>{u.get("xp", 0)} XP</b></p>'
    f'</div>',
    unsafe_allow_html=True
)

# Page selections
nav_options = [
    "3D Globe View",
    "Country Dossiers",
    "Compare Mode",
    "India Special Module",
    "Quiz Engine",
    "Study Desk",
    "Current Affairs"
]

# Admin Check
if u.get("is_admin", False):
    nav_options.append("Admin Panel")

st.session_state["current_page"] = st.sidebar.radio("Navigation Menu", nav_options, index=nav_options.index(st.session_state["current_page"]))

st.sidebar.markdown("---")
if st.sidebar.button("🔓 Sign Out"):
    logout()
    st.rerun()

# --- PAGE ROUTING CONTROLLER ---
try:
    if st.session_state["current_page"] == "3D Globe View":
        render_globe_view()
    elif st.session_state["current_page"] == "Country Dossiers":
        render_country_details()
    elif st.session_state["current_page"] == "Compare Mode":
        render_compare_mode()
    elif st.session_state["current_page"] == "India Special Module":
        render_india_special()
    elif st.session_state["current_page"] == "Quiz Engine":
        render_quiz_engine()
    elif st.session_state["current_page"] == "Study Desk":
        render_study_desk()
    elif st.session_state["current_page"] == "Current Affairs":
        render_current_affairs()
    elif st.session_state["current_page"] == "Admin Panel":
        render_admin_panel()
except Exception as e:
    st.error(f"Failed to render the selected module: {e}")
