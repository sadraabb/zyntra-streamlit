#-- IMPORTS ---
import streamlit as st
from styles.styles import apply_styles

def config_page_titles():
    st.set_page_config(
        page_title="Zyntra | Interactive Games",
        page_icon="🕹️",
        layout="centered"
    )
    st.title("بازی‌ها و سرگرمی‌های تعاملی Zyntra")
# بررسی وضعیت ثبت نام
if "registered" not in st.session_state or not st.session_state["registered"]:
    st.error("🚨 برای ورود به این صفحه باید ابتدا ثبت‌نام کنید!")
    st.stop()
else:
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



if __name__ == "__main__":
    # Apply custom styles
    apply_styles()
    # Configure page titles and layout
    config_page_titles()