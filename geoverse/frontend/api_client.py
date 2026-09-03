import requests
import streamlit as st
from typing import Optional, Dict, Any, List

API_BASE_URL = "http://127.0.0.1:8000"

def get_headers() -> Dict[str, str]:
    headers = {}
    if "token" in st.session_state and st.session_state["token"]:
        headers["Authorization"] = f"Bearer {st.session_state['token']}"
    return headers

def make_request(method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Optional[Any]:
    url = f"{API_BASE_URL}{endpoint}"
    headers = get_headers()
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            return None
            
        if response.status_code == 401:
            # Token expired or invalid, reset auth state
            st.session_state["token"] = None
            st.session_state["user"] = None
            return None
            
        if response.status_code in [200, 201]:
            try:
                return response.json()
            except ValueError:
                return response.text
        else:
            return None
    except Exception as e:
        st.error(f"Network error communicating with API: {e}")
        return None

# Auth helper APIs
def login(username: str, password: str) -> bool:
    url = f"{API_BASE_URL}/api/auth/token"
    try:
        response = requests.post(url, data={"username": username, "password": password})
        if response.status_code == 200:
            res_data = response.json()
            st.session_state["token"] = res_data["access_token"]
            # Fetch user profile
            profile = make_request("GET", "/api/auth/me")
            if profile:
                st.session_state["user"] = profile
                return True
        return False
    except Exception as e:
        st.error(f"Login failed: {e}")
        return False

def register(username: str, email: str, password: str) -> Optional[Dict[str, Any]]:
    url = f"{API_BASE_URL}/api/auth/register"
    try:
        response = requests.post(url, json={"username": username, "email": email, "password": password})
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 400:
            err = response.json()
            st.error(f"Registration failed: {err.get('detail', 'Unknown error')}")
            return None
        return None
    except Exception as e:
        st.error(f"Registration failed: {e}")
        return None

def logout():
    st.session_state["token"] = None
    st.session_state["user"] = None
    st.session_state["current_page"] = "3D Globe View"
