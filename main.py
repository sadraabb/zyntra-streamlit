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
import sqlite3
import time
from styles import apply_styles,show_logo
from config import main_page_config
from database.userpanel import add_user, create_users_table
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
        "user_name" : "",
        "name" : "",
        "last_name" : "",
        "password" : "",
        "email" : "",
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
# login form
def login_form():
    with st.form("login_form"):
        pass
# Create Register Form
def create_register_form():
    if st.session_state.get("registered") == True:
        # یک اطلاع رسانی کوتاه متنی بابت اتمام مراحل ثبت نام و عدم نیاز به ثبت نام
        st.balloons()
        st.write(f"خوش آمدی {st.session_state['name']} عزیز! ✨")
        if st.button("ورود به دنیای زینترو 🚀"):
            st.switch_page(page="pages/1_home.py")
    else:
        with st.form("register_form"):
            warning_show = st.warning(
                """
                **توجه:**
                 
                   این پروژه در حال حاضر در حالت آزمایشی (Demo) قرار دارد.  
                     لطفاً از وارد کردن اطلاعات واقعی یا شخصی خودداری کرده و از داده‌های نمونه و ساختگی استفاده نمایید،  
                       زیرا اطلاعات واردشده در پایگاه داده ذخیره می‌شوند.
                """,
                icon="🚨"
                )

            #id_number = st.number_input("آیدی عددی", value=user_id, disabled=True,key="reg_user_id")
            name = st.text_input(label="نام *" , placeholder="لطفا نام خود را بنویسید برای مثال : صدرا" , key="reg_name")
            last_name = st.text_input(label="نام خانوادگی *",placeholder="لطفا نام خانوادگی خود را بنویسید برای مثال : عباس زاده" , key="reg_last_name")
            user_name = st.text_input(label="نام کاربری *",placeholder="لطفا یک نام کاربری برای خود بنویسید برای مثال : sadraabb",key="reg_username")
            email_address = st.text_input(label="ایمیل",placeholder="لطفا ایمیل خود را وارد کنید برای مثال : abbsadra@gmail.com",key="reg_email")
            password_user = st.text_input(label="رمز عبور *",type="password",placeholder="لطفا یک رمز عبور قوی برای خود انتخاب کنید",key="reg_password")
            check_rules = st.checkbox("پذیرفتن قوانین *",help="برای ادامه باید قوانین رو بپذیرید",key="reg_accept_rules")
            sumbit_button = st.form_submit_button("ثبت نام در برنامه")
            if sumbit_button:
                st.session_state["reg_submitted"] = True
# Function for register process
def process_register():
    if not st.session_state["reg_submitted"]:
        return
    user_name = st.session_state["reg_username"]
    password = st.session_state["reg_password"]
    name = st.session_state["reg_name"]
    last_name = st.session_state["reg_last_name"]
    check_rules = st.session_state["reg_accept_rules"]
    # --- VALIDATION CHECKS ---
    if not user_name:
        st.error("لطفا یوزرنیم خود را وارد کنید!")
    elif not password:
        st.error("لطفا رمز عبور خود را وارد کنید!")
    elif not name:
        st.error("لطفا نام خود را وارد کنید!")
    elif not last_name:
        st.error("لطفا نام خانوادگی خود را وارد کنید!")
    elif not check_rules:
        st.error("برای ادامه باید قوانین رو بپذیرید")
    elif all (st.session_state[key] for key in ["reg_username","reg_name","reg_last_name","reg_accept_rules"]):
        with st.spinner("در حال ثبت‌نام... 🎮"):
            session_state_mange_success_register()
            add_user(
                user_name=st.session_state["reg_username"],
                name=st.session_state["reg_name"],
                last_name=st.session_state["reg_last_name"],
                password=st.session_state["reg_password"],
                email=st.session_state.get("reg_email","")
            )
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
        "name" : st.session_state["reg_name"],
        "last_name" : st.session_state["reg_last_name"],
        "password" : st.session_state["reg_password"],
        "email" : st.session_state.get("reg_email",""),
        "check_rules" : st.session_state["reg_accept_rules"],
        "reg_submitted" : False
    }
    for key, value in finish_detailed.items():
        st.session_state[key] = value
# --- MAIN PAGE RUNNER ---
def run_page():
    create_users_table()
    init_page_state()
    create_register_form()
    process_register()
# ============ EXECUTION ============
bootstrap_main_page()
run_page()
# ==================================