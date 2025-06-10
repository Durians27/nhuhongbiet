import streamlit as st
import random

# Khởi tạo số ngẫu nhiên nếu chưa có
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""

# Giao diện
st.title("🎲 Game Đoán Số (1 - 100)")
st.write("Tôi đã chọn một số trong khoảng từ 1 đến 100. Bạn đoán thử xem là số nào!")

# Người chơi nhập số
guess = st.number_input("Nhập số bạn đoán:", min_value=1, max_value=100, step=1)

# Nút đoán
if st.button("🔍 Đoán"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.session_state.result = "📉 Số bạn đoán nhỏ hơn!"
    elif guess > st.session_state.number:
        st.session_state.result = "📈 Số bạn đoán lớn hơn!"
    else:
        st.session_state.result = f"🎉 Chính xác rồi! Bạn đã đoán đúng sau {st.session_state.attempts} lần thử."
        st.session_state.number = None  # reset game

# Hiển thị kết quả
st.write(st.session_state.result)

# Nút chơi lại
if st.button("🔁 Chơi lại"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.result = ""
    st.experimental_rerun()
