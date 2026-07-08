import streamlit as st
import random
import time

# Page setup for BASS
st.set_page_config(page_title="Albedrío - BASS")

# Session state initialization
if 'resultat' not in st.session_state:
    st.session_state.resultat = None

# Interface logic
if st.session_state.resultat is None:
    # Fem servir HTML per fer el botó més gran i visual
    # Encapsulem el botó en un div amb estil
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #000000;
            color: white;
            font-size: 24px;
            height: 3em;
            width: 100%;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("ROLL THE DICE"):
        with st.spinner('Processing...'):
            time.sleep(1.5)
            # Triem entre els dos símbols
            st.session_state.resultat = random.choice(["⚁", "⚃"])
            st.rerun()

else:
    # Mostrar el símbol gran
    st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{st.session_state.resultat}</h1>", unsafe_allow_html=True)
    st.success("Your action has been processed and locked.")
    st.markdown("**The system has determined your path.**")
