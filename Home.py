# File: Home.py
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image

st.set_page_config(page_title="Supplier Portal Login", layout="wide")

# Dummy credentials
credentials = {
    "usernames": {
        "alice": {"name": "Alice Brown", "password": stauth.Hasher(["pass1"]).generate()[0]},
        "bob": {"name": "Bob Smith", "password": stauth.Hasher(["pass2"]).generate()[0]},
        "carol": {"name": "Carol Jones", "password": stauth.Hasher(["pass3"]).generate()[0]},
        "david": {"name": "David Liu", "password": stauth.Hasher(["pass4"]).generate()[0]},
        "eve": {"name": "Eve Patel", "password": stauth.Hasher(["pass5"]).generate()[0]}
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "proc_platform", "abcdef", cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("""
        <div style="height:100vh; background-color:#1E73E8; display:flex; justify-content:center; align-items:center;">
            <h1 style="color:white; font-size:30px;">Welcome to Our Procurement Platform</h1>
        </div>
    """, unsafe_allow_html=True)

with col2:
    if authentication_status:
        st.success(f"Welcome {name}!")
        st.markdown("### Use the sidebar to navigate through the portal.")
    elif authentication_status is False:
        st.error("Invalid username or password")
    elif authentication_status is None:
        st.warning("Please enter your credentials")
