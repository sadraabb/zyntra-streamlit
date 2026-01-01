# styles.py
import streamlit as st

def apply_styles():
    st.logo("assets/logo/Zyntra-logo.png",size="large")
    style_code = """
    <style>
        /* کل اپلیکیشن و body */
        body, .stApp, div, span, p, h1, h2, h3, h4, h5, h6 {
            direction: rtl;
            text-align: right;
            font-family: 'Vazir', sans-serif;  /* فونت فارسی استاندارد */
        }

        /* پس‌زمینه و افکت */
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                        url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
        }

        /* فیلدهای ورودی */
        input, textarea {
            direction: rtl;
            text-align: right;
        }

        /* فرم شیشه‌ای */
        div[data-testid="stForm"] {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        /* رنگ هدرها */
        h1, h2, h3, h4, h5, h6 {
            color: #00f2fe;
            text-shadow: 2px 2px 4px #000000;
        }

        /* دکمه اختصاصی Zyntra */
        button[kind="primaryFormSubmit"] {
            background-color: #00f2fe !important;
            color: black !important;
            font-weight: bold !important;
            width: 100%;
        }
    </style>
    """
    st.markdown(style_code, unsafe_allow_html=True)
