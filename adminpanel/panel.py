import sys
import os

# این بخش بسیار مهم است: پیدا کردن مسیر اصلی پروژه
current_dir = os.path.dirname(os.path.abspath(__file__)) # مسیر پوشه adminpanel
project_root = os.path.dirname(current_dir)             # مسیر پوشه zyntra (یک پله عقب‌تر)

# اضافه کردن مسیر اصلی به حافظه پایتون برای جستجوی ماژول‌ها
if project_root not in sys.path:
    sys.path.append(project_root)
import streamlit as st
import sqlite3
from styles.styles import apply_panel_admin_styles
from config.page_config import admin_panel_config

#--- PAGE CONTENT ---
def bootstrap_admin_panel_page():
    admin_panel_config()
    apply_panel_admin_styles()

def login_admin_panel():
    st.title("پنل مدیریت زینترا",width="content")
    with st.form("Admin_Login_form"):
        pass
def run_app():
    bootstrap_admin_panel_page()
    login_admin_panel()


run_app()