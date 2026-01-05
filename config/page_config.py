import streamlit as st

# --- PAGE CONFIGURATION ---
def main_page_config():
 #Program Title
     st.set_page_config(
         page_title="Zyntra | Registration",
        page_icon="🎮",
          layout="centered"
     )
def home_page_config():
    st.set_page_config(
        page_title="Zyntra | Interactive Games",
        page_icon="🕹️",
        layout="centered"
    )

def feedback_page_config():
    st.set_page_config(
        page_title="Zyntra | Feedback",
        page_icon="💬",
        layout="centered"
    )

def guesslab_page_config():
    st.set_page_config(
        page_title="Zyntra | GuessLab Game",
        page_icon="🧩",
        layout="centered"
    )

def admin_panel_config():
    st.set_page_config(
        page_title="Zyntra | Admin Panel",
        page_icon="🔧",
        layout="centered"
    )
# --- END OF PAGE CONFIGURATION ---