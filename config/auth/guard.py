import streamlit as st

def require_login():
    if not st.session_state.get("loginned"):
        st.error("🚨 برای دسترسی باید وارد حساب کاربری شوید")
        if st.button("ورود به بخش ثبت نام/لاگین"):
            st.switch_page("main.py")
        st.stop()