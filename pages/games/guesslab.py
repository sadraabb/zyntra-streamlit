import streamlit as st
import sys
import os

# اضافه کردن مسیر پروژه (همون جایی که main.py هست) به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from styles.styles import apply_styles
from config.page_config import guesslab_page_config

# --- PAGE CONTENT ---
def bootstrap_guesslab_page():
    guesslab_page_config()
    apply_styles()
bootstrap_guesslab_page()
# --- GUESSLAB PAGE CONTENT ---
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")