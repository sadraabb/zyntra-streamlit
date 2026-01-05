import streamlit as st
import sqlite3
from styles.styles import apply_styles,show_logo
from config.page_config import feedback_page_config
# --- PAGE CONTENT ---
def bootstrap_feedback_page():
    feedback_page_config()
    apply_styles()
    show_logo()
# --- FEEDBACK PAGE CONTENT ---
def display_feedback_page():
    st.title("بازخورد و پیشنهادات شما")
    st.markdown(
        """
        از اینکه وقت می‌گذارید و بازخورد خود را با ما به اشتراک می‌گذارید، سپاسگزاریم!  
        لطفاً نظرات، پیشنهادات یا هرگونه مشکلی که در استفاده از برنامه با آن مواجه شده‌اید را در فرم زیر وارد کنید.  
        ما به دقت همه بازخوردها را بررسی می‌کنیم تا تجربه کاربری بهتری ارائه دهیم.
        """
    )
    feedback = st.text_area("لطفاً بازخورد خود را اینجا بنویسید:", height=200)
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    st.markdown("امتیاز کلی شما به تجربه کاربری برنامه:")
    selected = st.feedback("stars")
    if st.button("ارسال بازخورد"):
        if feedback.strip() == "":
            st.error("لطفاً قبل از ارسال، بازخورد خود را وارد کنید.")
        elif selected is None:
            st.error("لطفاً یک امتیاز انتخاب کنید.")
        else:
            # در اینجا می‌توانید کد ذخیره‌سازی یا ارسال بازخورد را اضافه کنید
            st.success("بازخورد شما با موفقیت ارسال شد! از همکاری شما سپاسگزاریم.")
# ============ EXECUTION ============
bootstrap_feedback_page()
display_feedback_page()
# ==================================