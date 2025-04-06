# File: Home.py
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image

st.set_page_config(page_title="Supplier Portal Login", layout="wide")

# Dummy credentials
credentials = {
    "usernames": {
        "alice": {
            "name": "Alice Brown",
            "password": "$2b$12$DAoq7hLvxcaNa9E6pgvl6OLH5QrEywY.ZVvTfepvlmwDZDmg.G8W2"
        },
        "bob": {
            "name": "Bob Smith",
            "password": "$2b$12$/6wYVO/.9n6PwmHSV.fT5.XjpHMXNaH0JE4mERWLksdrjdHcLfsEy"
        },
        "carol": {
            "name": "Carol Jones",
            "password": "$2b$12$vgMIuY8xnWI7OZ7XSHbDSOIO9ttVySTUG0FyRRfrYMNHoarCEoQyq"
        },
        "david": {
            "name": "David Liu",
            "password": "$2b$12$MtvIdMwsagRHEy0OSEhuWuBIV8cEt/4UjNs9jx5bGCdLHYNuJ0rHO"
        },
        "eve": {
            "name": "Eve Patel",
            "password": "$2b$12$.vHRaCKQNSuSbtG7pOvp4OZM76vvkKlGVz81WtUKKoBKbq.Pew.f6"
        }
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
