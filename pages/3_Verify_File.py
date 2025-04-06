import streamlit as st
import hashlib

st.title("🔍 Verify File Integrity")

def calculate_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

verify_file = st.file_uploader("Select File to Verify")
if verify_file:
    hash_val = calculate_hash(verify_file.read())
    matches = [b for b in st.session_state.blockchain if b['file_hash'] == hash_val]
    if matches:
        b = matches[0]
        st.success(f"✅ Verified: Block #{b['index']} uploaded by {b['uploader']} on {b['timestamp']}")
    else:
        st.error("❌ File not found in the blockchain.")

