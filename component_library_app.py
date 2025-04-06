# component_library_app.py
import streamlit as st
import hashlib
import os
from datetime import datetime

# Initialize blockchain in session state if not present
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# Blockchain Functions
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

# Streamlit App
st.title("📁 Component Details Library with Blockchain")
st.write("Upload and verify component files using blockchain hashes.")

# Upload Section
st.header("🔼 Upload Component File")
file = st.file_uploader("Choose a CAD/Certificate file", type=["pdf", "step", "stl", "jpg", "png", "txt"])
uploader_name = st.text_input("Your Name")

if file and uploader_name:
    file_bytes = file.read()
    file_hash = calculate_hash(file_bytes)
    if st.button("Upload & Register on Blockchain"):
        create_block(file.name, file_hash, uploader_name)
        st.success(f"File '{file.name}' uploaded and recorded with hash: {file_hash}")

# Blockchain View
st.header("📜 Blockchain Ledger")
for block in reversed(st.session_state.blockchain):
    with st.expander(f"Block #{block['index']} - {block['file_name']}"):
        st.json(block)

# Integrity Check
st.header("🔍 Verify File Integrity")
verify_file = st.file_uploader("Upload a file to verify", type=["pdf", "step", "stl", "jpg", "png", "txt"], key="verify")

if verify_file:
    file_bytes = verify_file.read()
    file_hash = calculate_hash(file_bytes)
    matches = [b for b in st.session_state.blockchain if b['file_hash'] == file_hash]
    if matches:
        st.success(f"✅ File matches block #{matches[0]['index']} uploaded by {matches[0]['uploader']} on {matches[0]['timestamp']}.")
    else:
        st.error("❌ File hash not found in blockchain. Possible tampering or unregistered file.")
