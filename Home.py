import streamlit as st

st.set_page_config(page_title="Home - World Cities MIS", page_icon="🏙️")

st.title("World Cities MIS")
st.write("Welcome to the World Cities MIS Streamlit app. This home page gives a short intro and a quick way to open the main app page.")

st.markdown("### What this does")
st.write(
    "Click the button below to navigate to the main app page (the file you placed in the pages folder as app.py)."
)

def _navigate_to_app():
    # Try programmatic navigation using query params (works in many Streamlit versions)
    try:
        st.experimental_set_query_params(page="App")
        st.experimental_rerun()
    except Exception:
        # If programmatic navigation isn't permitted, nothing fatal — we'll show a link below.
        pass

if st.button("Open App"):
    _navigate_to_app()

st.markdown("---")
st.write("If the button doesn't change pages in your environment, use this link instead:")
st.markdown("[Open App page](./?page=App)")
