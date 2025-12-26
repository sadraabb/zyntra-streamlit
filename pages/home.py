#-- IMPORTS ---
import streamlit as st
from styles.styles import apply_styles
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



if __name__ == "__main__":
    # Apply custom styles
    apply_styles()