"""
    ┌───────────────────────────────────────────────────────────────────────┐
    │  🎮 ZYNTRA | INTERACTIVE WEB EXPERIENCE PLATFORM                      │
    │  Copyright (c) 2025 Sadra Abb. All Rights Reserved.                   │
    │                                                                       │
    │  LICENSED UNDER THE MIT OPEN-SOURCE PERMISSIVE LICENSE                │
    └───────────────────────────────────────────────────────────────────────┘

    Permission is hereby granted, free of charge, to any person obtaining a 
    copy of this software and associated documentation files (the "Software"), 
    to deal in the Software without restriction, including without limitation 
    the rights to use, copy, modify, merge, publish, distribute, sublicense, 
    and/or sell copies of the Software.

    📜 THE PLAYBOOK (Terms):
    -------------------------------------------------------------------------
    1. THE ARCHITECT: The above copyright notice and this permission notice 
       shall be included in all copies or substantial portions of the Software.
    
    2. THE VISION: Zyntra is a playground for interactive web games and 
       digital experiments. Explore, modify, and level up the web! 🚀

    -------------------------------------------------------------------------
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
    DEALINGS IN THE SOFTWARE.

    ⚡ "Keep coding, keep playing, keep evolving." – Sadra Abbaszadeh
"""

__meta__ = {
    "Project": "Zyntra",
    "Author": "Sadra Abbaszadeh",
    "Type": "Interactive Web App",
    "License": "MIT"
}

#imports
import streamlit as st
import random as rd
import time
from styles.styles import apply_styles,show_logo
from config.page_config import main_page_config
from st_pages import add_page_title, get_nav_from_toml
# --- PAGE TITLE ---
st.title("برنامه بازی های سرگرمی تحت وب",width="content")
# --- CONFIGURATION & STYLING ---
def bootstrap_main_page():
    main_page_config()
    apply_styles()
    show_logo()
# --- SESSION STATE MANAGEMENT ---
def init_session_state():
    default_data = {
        "registered" : False,
        "user_id" : "",
        "user_name" : "",
        "name" : "",
        "last_name" : "",
        "check_rules" : False,
        "reg_submitted" : False
    }
    for key,value in default_data.items():
        if key not in st.session_state:
            st.session_state[key] = value
# --- SESSION STATE INITIALIZATION ---
def init_page_state():
    if "registered" not in st.session_state:
        init_session_state()
# def configure_page():
#     # #Program Title
#     st.title("برنامه بازی های سرگرمی تحت وب",width="content")
#     st.set_page_config(
#         page_title="Zyntra | Registration",
#         page_icon="🎮",
#           layout="centered"
#     )
#     # راست‌چین کردن صفحه 
#     st.markdown(
#         """
#         <style>
#         /* راست‌چین کردن همه المان‌های Streamlit */
#         .stApp {
#         direction: rtl;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#         )
#     st.markdown(
#         """
#         <style>
#         input {
#         direction: rtl;
#         text-align: right;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#         )
    

# def apply_custom_design():
#     st.markdown(
#         """
#         <style>
#         /* تنظیم تصویر پس‌زمینه */
#         .stApp {
#             background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
#                         url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80");
#             background-size: cover;
#         }

#         /* استایل دادن به فرم (حالت شیشه‌ای) */
#         div[data-testid="stForm"] {
#             background-color: rgba(255, 255, 255, 0.05);
#             border-radius: 15px;
#             padding: 20px;
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             backdrop-filter: blur(10px);
#         }

#         /* تغییر رنگ تایتل و متون */
#         h1 {
#             color: #00f2fe;
#             text-shadow: 2px 2px 4px #000000;
#             text-align: center;
#         }
        
#         /* استایل دکمه ثبت نام */
#         button[kind="primaryFormSubmit"] {
#             background-color: #00f2fe !important;
#             color: black !important;
#             font-weight: bold !important;
#             width: 100%;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# --- REGISTER FORM CREATION ---
# Create Register Form
def create_form():
    default_return = (None, None, None, None, None, None)
    if st.session_state["registered"]:
        # یک اطلاع رسانی کوتاه متنی بابت اتمام مراحل ثبت نام و عدم نیاز به ثبت نام
        st.balloons()
        st.write(f"خوش آمدی {st.session_state['name']} عزیز! ✨")
        if st.button("ورود به دنیای زینترو 🚀"):
            st.switch_page(page="pages/1_home.py")
        return default_return
    else:
        with st.form("register_form"):
            user_id = rd.randint(1000,52534)
            warning_show = st.warning("این یک پروژه نمونه میباشد! اطلاعات شما ذخیره نمیشود!",icon="🚨")
            id_number = st.number_input("آیدی عددی", value=user_id, disabled=True,key="reg_user_id")
            user_name = st.text_input(label="نام کاربری *",placeholder="لطفا یک نام کاربری برای خود بنویسید برای مثال : sadraabb",key="reg_username")
            name = st.text_input(label="نام *" , placeholder="لطفا نام خود را بنویسید برای مثال : صدرا" , key="reg_name")
            last_name = st.text_input(label="نام خانوادگی *",placeholder="لطفا نام خانوادگی خود را بنویسید برای مثال : عباس زاده" , key="reg_last_name")
            check_rules = st.checkbox("پذیرفتن قوانین *",help="برای ادامه باید قوانین رو بپذیرید",key="reg_accept_rules")
            sumbit_button = st.form_submit_button("ثبت نام در برنامه")
            if sumbit_button:
                st.session_state["reg_submitted"] = True
            return user_id,user_name,name,last_name,sumbit_button,check_rules
# Function for register process
def process_register():
    if not st.session_state["reg_submitted"]:
        return
    if not st.session_state["reg_username"]:
        st.error("لطفا یوزرنیم خود را وارد کنید!")
    elif not st.session_state["reg_name"]:
        st.error("لطفا نام خود را وارد کنید!")
    elif not st.session_state["reg_last_name"]:
        st.error("لطفا نام خانوادگی خود را وارد کنید!")
    elif not st.session_state["reg_accept_rules"]:
        st.error("برای ادامه باید قوانین رو بپذیرید")
    elif all (st.session_state[key] for key in ["reg_username","reg_name","reg_last_name","reg_accept_rules"]):
        with st.spinner("در حال ثبت‌نام... 🎮"):
            session_state_mange_success_register()
            time.sleep(2)
            st.rerun()

# Function to update session state after successful registration
# This function sets the user's registration status and saves all relevant user info 
# into Streamlit's session_state so it can be accessed across pages or reruns.
# Parameters:
#   user_name (str): The username entered by the user
#   name (str): The user's first name
#   last_name (str): The user's last name
#   check_rules (bool): Whether the user accepted the rules/terms
def session_state_mange_success_register():
    finish_detailed = {
        "registered" : True,
        "user_name" : st.session_state["reg_username"],
        "user_id" : st.session_state["reg_user_id"],
        "name" : st.session_state["reg_name"],
        "last_name" : st.session_state["reg_last_name"],
        "check_rules" : st.session_state["reg_accept_rules"],
        "reg_submitted" : True
    }
    for key, value in finish_detailed.items():
        st.session_state[key] = value
# --- MAIN PAGE RUNNER ---
def run_page():
    create_form()
    process_register()
# ============ EXECUTION ============
bootstrap_main_page()
init_page_state()
run_page()
# ==================================