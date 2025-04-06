import streamlit as st
st.title("📜 Blockchain Ledger")

if 'blockchain' not in st.session_state or not st.session_state.blockchain:
    st.info("No blocks in the ledger yet. Upload files to start building the blockchain.")
else:
    for block in reversed(st.session_state.blockchain):
        with st.expander(f"Block #{block['index']} - {block['file_name']}"):
            st.json(block)
