import streamlit as st
import sqlite3
from styles import apply_styles,show_logo
from config import feedback_page_config
from config.auth import require_login
from database.userpanel import save_feedback,init_feedback_db

init_feedback_db()
if "step_conf_feed" not in st.session_state:
    st.session_state.step_conf_feed = 1


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
        سلام {name} عزیز\n
          از اینکه وقت می‌گذارید و بازخورد خود را با ما به اشتراک می‌گذارید، سپاسگزاریم!  
            لطفاً نظرات، پیشنهادات یا هرگونه مشکلی که در استفاده از برنامه با آن مواجه شده‌اید را در فرم زیر وارد کنید.  
              ما به دقت همه بازخوردها را بررسی می‌کنیم تا تجربه کاربری بهتری ارائه دهیم.
        """.format(name=st.session_state.get("name", "کاربر"))
        )
    feedback = st.text_area("لطفاً بازخورد خود را اینجا بنویسید:", height=200)
    issue_type = st.selectbox(
    "کدام بخش برای شما مشکل داشته است؟",
    ["همه چیز خوب است", "کارایی", "ظاهر برنامه", "سرعت", "ویژگی‌های جدید"]
)
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    st.markdown("امتیاز کلی شما به تجربه کاربری برنامه:")
    selected = st.feedback("stars")
    if st.button("ارسال بازخورد"):
        if feedback.strip() == "":
            st.error("لطفاً قبل از ارسال، بازخورد خود را وارد کنید.")
        elif selected is None:
            st.error("لطفاً یک امتیاز انتخاب کنید.")
        else:
            st.session_state.feedback_text = feedback
            st.session_state.issue_type = issue_type
            st.session_state.rating = selected
            confirm_feedback_dialog()

@st.dialog("تایید ارسال بازخورد")
def confirm_feedback_dialog():
    step = st.session_state.step_conf_feed
    if step == 1 :
        st.write("آیا مطمئن هستید که می‌خواهید بازخورد ارسال شود؟")
        if st.button("✅ ارسال شود"):
            st.write("تست")
            st.session_state.step_conf_feed = 2
            st.rerun()
        elif st.button("لغو"):
            st.write("هیچ نگرانی نیست! بازخوردی ارسال نشده و می‌توانید بعداً دوباره امتحان کنید.")
            st.session_state.step_conf_feed = 1
    elif step == 2:
        st.markdown(
            """
کاربر {name} عزیز \n
با تشکر از شما ،نظر با ارزشتان را دریافت کردیم
""".format(name=st.session_state.get("name", "کاربر"))
        )
        st.session_state.step_conf_feed = 3
    elif step == 3:
        save_feedback(
            st.session_state.get("name","کاربر"),
            st.session_state.get("feedback_text", "feedback"),
            st.session_state.get("issue_type", "issue_type"),
            st.session_state.get("rating","stars")
        )
# ============ EXECUTION ============
bootstrap_feedback_page()
require_login()
display_feedback_page()
# ==================================