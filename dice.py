import streamlit as st
import random
import time

# Page setup for BASS
st.set_page_config(page_title="Albedrío - BASS", page_icon="🎲")

st.title("🎲 Albedrío")
st.subheader("Agency vs. Code: An illusionary experience")

# Session state initialization
if 'resultat' not in st.session_state:
    st.session_state.resultat = None

# Interface logic
if st.session_state.resultat is None:
    # Placeholder for your dice image
    try:
        st.image("dau.png", width=150)
    except:
        st.write("---")

    if st.button("Roll the dice"):
        with st.spinner('Processing your choice...'):
            time.sleep(1.5)
            # The system restricts the outcome to 2 or 4
            st.session_state.resultat = random.choice([2, 4])
            st.rerun()

else:
    # No way back. The button is gone forever.
    st.header(f"System Output: {st.session_state.resultat}")
    st.success("Your action has been processed and locked.")
    st.markdown("**The system has determined your path. There is no alternative.**")
