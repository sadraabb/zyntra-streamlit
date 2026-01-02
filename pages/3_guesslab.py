#-- IMPORTS ---
import streamlit as st
import sys
import os
import random as rd
import time

# اضافه کردن مسیر پروژه (همون جایی که main.py هست) به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
#import styles and config
from styles.styles import apply_styles
from config.page_config import guesslab_page_config

# --- PAGE CONTENT ---
def bootstrap_guesslab_page():
    guesslab_page_config()
    apply_styles()
bootstrap_guesslab_page()
# --- GUESSLAB PAGE RUN MANGMENT ---#
def run_guesslab_page():
    if not check_registration():
        st.error("🚨 برای ورود به این صفحه باید ابتدا ثبت‌نام کنید!")
        st.stop()
    else:
        guesslab_game()
# --- Registration Check ---
def check_registration() -> bool:
# بررسی وضعیت ثبت نام
    return "registered" in st.session_state and st.session_state["registered"]
# --- GUESSLAB PAGE CONTENT ---
def guesslab_game():
    pass


run_guesslab_page()