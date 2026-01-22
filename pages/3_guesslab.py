#-- IMPORTS ---
import streamlit as st
import random as rd
import time
#import styles and config
from styles import apply_styles
from config.auth import require_login
from config import guesslab_page_config
st.title("بازی حدس اعداد - GuessLab",width="content")
# --- PAGE CONTENT ---
def bootstrap_guesslab_page():
    guesslab_page_config()
    apply_styles()
bootstrap_guesslab_page()

# --- GUESSLAB PAGE CONTENT ---
def guesslab_game():
    st.markdown("## قوانین بازی:")
    st.markdown("""
    - یک عدد تصادفی بین 1 تا 100 انتخاب شده است.
    - شما 10 تلاش برای حدس زدن این عدد دارید.
    - پس از هر حدس، به شما گفته می‌شود که عدد حدس زده شده بزرگتر یا کوچکتر از عدد واقعی است.
    """)
    
    # --- مقداردهی اولیه ---
    if "random_number" not in st.session_state:
        st.session_state.random_number = rd.randint(1,100)
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    # --- اصلاح اول: نمایش تاریخچه باید بیرون از شرط‌ها باشد تا همیشه دیده شود ---
    for msg in st.session_state.chat_history:
        st.chat_message(msg['role']).write(msg['content'])

    max_attempts = 10
    
    if not st.session_state.game_over:
        user_guess = st.chat_input("عدد خود را حدس بزنید (بین 1 تا 100):")
        if user_guess:
            # ذخیره حدس کاربر
            st.session_state.chat_history.append({"role": "user", "content": user_guess})
            
            try:
                guess = int(user_guess)
                st.session_state.attempts += 1
                
                if guess == st.session_state.random_number:
                    reply = f"🎉 آفرین! عدد {st.session_state.random_number} را درست حدس زدی در {st.session_state.attempts} تلاش."
                    st.session_state.chat_history.append({"role": "ai", "content": reply})
                    # آماده‌سازی برای بازی بعدی
                    st.session_state.random_number = rd.randint(1,100)
                    st.session_state.attempts = 0
                    st.session_state.chat_history.append({"role": "ai", "content": "عدد جدید انتخاب شد! دوباره حدس بزن."})
                
                elif guess < st.session_state.random_number:
                    reply = "حدس شما کوچکتر از عدد مورد نظر هست"
                    st.session_state.chat_history.append({"role": "ai", "content": reply})
                
                elif guess > st.session_state.random_number:
                    reply = "حدس شما بزرگتر از عدد مورد نظر هست"
                    st.session_state.chat_history.append({"role": "ai", "content": reply})

                # بررسی اتمام شانس
                if st.session_state.attempts >= max_attempts and guess != st.session_state.random_number:
                    st.error(f"😢 بازی تمام شد! عدد درست {st.session_state.random_number} بود.")
                    st.session_state.game_over = True
                
                # اصلاح دوم: استفاده از rerun برای نمایش فوری نتایج در چت
                st.rerun()

            except ValueError:
                st.warning("لطفا یک عدد وارد کنید")
    else:
        st.write("تعداد شانس های شما به پایان رسیده است")
        if st.button("شروع مجدد 🔄"):
            st.session_state.game_over = False
            st.session_state.attempts = 0
            st.session_state.chat_history = []
            st.rerun()

require_login()
guesslab_game()