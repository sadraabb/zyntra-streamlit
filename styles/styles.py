# styles.py
import streamlit as st

def apply_styles():
    style_code = """
    <style>
        /* کل اپلیکیشن */
        .stApp {
            direction: rtl;
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                        url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
        }

        /* فیلدهای ورودی */
        input {
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

        /* تایتل‌ها */
        h1 {
            color: #00f2fe;
            text-shadow: 2px 2px 4px #000000;
            text-align: center;
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