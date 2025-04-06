import streamlit as st
st.set_page_config(page_title="Honeywell Supplier Portal", layout="wide")

st.title("🛠️ Honeywell Supplier Collaboration Platform")
st.write("Welcome to the Supplier Collaboration Portal. Navigate through the sidebar to explore features like file uploads, performance dashboards, and inventory tracking.")

st.image("https://www.honeywell.com/content/dam/honeywell/honeywell-images/backgrounds/industry-aerospace.jpg", use_column_width=True)


# ──────── File: pages/1_Upload_Component.py ────────
import streamlit as st
import hashlib
from datetime import datetime

st.title("📁 Upload Component Details")

if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

def calculate_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

def create_block(file_name, file_hash, uploader):
    block = {
        'index': len(st.session_state.blockchain) + 1,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'file_name': file_name,
        'file_hash': file_hash,
        'uploader': uploader,
        'previous_hash': st.session_state.blockchain[-1]['block_hash'] if st.session_state.blockchain else '0'
    }
    block_string = f"{block['index']}{block['timestamp']}{block['file_name']}{block['file_hash']}{block['uploader']}{block['previous_hash']}"
    block['block_hash'] = hashlib.sha256(block_string.encode()).hexdigest()
    st.session_state.blockchain.append(block)

file = st.file_uploader("Upload Technical File / Certificate / CAD")
uploader = st.text_input("Uploaded By")

if file and uploader:
    hash_val = calculate_hash(file.read())
    if st.button("Upload & Register on Blockchain"):
        create_block(file.name, hash_val, uploader)
        st.success(f"Registered {file.name} with hash {hash_val}")

