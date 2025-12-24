import streamlit as st
# --- CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="Zyntra | Registration",
    page_icon="🎮",
    layout="centered"
)

def apply_custom_design():
    st.markdown(
        """
        <style>
        /* تنظیم تصویر پس‌زمینه */
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                        url("https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
        }

        /* استایل دادن به فرم (حالت شیشه‌ای) */
        div[data-testid="stForm"] {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        /* تغییر رنگ تایتل و متون */
        h1 {
            color: #00f2fe;
            text-shadow: 2px 2px 4px #000000;
            text-align: center;
        }
        
        /* استایل دکمه ثبت نام */
        button[kind="primaryFormSubmit"] {
            background-color: #00f2fe !important;
            color: black !important;
            font-weight: bold !important;
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_design()
# بررسی وضعیت ثبت نام
if "registered" not in st.session_state or not st.session_state["registered"]:
    st.error("🚨 برای ورود به این صفحه باید ابتدا ثبت‌نام کنید!")
    st.stop()
else:
    st.title("🎮 خوش آمدید به Zyntra – مرکز بازی‌ها", width="content")
    
    st.markdown(
        """
        سلام **{name}**!  
        در حال حاضر شما به سیستم وارد شده‌اید و می‌توانید به بازی‌ها و امکانات تعاملی آینده دسترسی داشته باشید.
        
        🕹️ این صفحه فعلاً در حال توسعه است، اما در آینده نزدیک امکانات زیر اضافه خواهند شد:
        - چندین بازی کوچک و سرگرم‌کننده
        - پروفایل کاربری با امتیاز و رکوردها
        - سیستم امتیازدهی و لیدربورد
        - امکانات تعامل با API و سرویس‌های خارجی
        """.format(name=st.session_state.get("name", "کاربر"))
    )
    
    st.info("🚧 این بخش هنوز در حال توسعه است. Coming Soon!")
    
    # دکمه ورود به بخش بازی‌ها (فعلاً غیر فعال)
    st.button("ورود به بازی‌ها (Coming Soon)", disabled=True)
