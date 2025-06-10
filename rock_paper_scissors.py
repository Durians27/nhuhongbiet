import streamlit as st
import random

# Thiết lập cấu hình trang
st.set_page_config(page_title="Trò chơi Kéo Búa Bao", layout="centered")

# Khởi tạo trạng thái trò chơi
if "score_player" not in st.session_state:
    st.session_state.score_player = 1
    st.session_state.score_computer = 5
    st.session_state.result = ""
    st.session_state.player_choice = None
    st.session_state.computer_choice = None

# Hàm xác định kết quả trò chơi
def determine_winner(player, computer):
    if player == computer:
        return "Hòa!"
    elif (player == "Kéo" and computer == "Bao") or \
         (player == "Búa" and computer == "Kéo") or \
         (player == "Bao" and computer == "Búa"):
        st.session_state.score_player += 1
        return "Bạn thắng!"
    else:
        st.session_state.score_computer += 1
        return "Máy thắng!"

# Hàm xử lý giao diện và logic trò chơi
def render_game():
    st.title("Trò chơi Kéo Búa Bao")
    
    # Hiển thị điểm số
    st.write(f"Điểm số - Bạn: {st.session_state.score_player} | Máy: {st.session_state.score_computer}")
    
    # Lựa chọn của người chơi
    st.write("Chọn hành động của bạn:")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Kéo", key="Kéo"):
            st.session_state.player_choice = "Kéo"
    with col2:
        if st.button("Búa", key="Búa"):
            st.session_state.player_choice = "Búa"
    with col3:
        if st.button("Bao", key="Bao"):
            st.session_state.player_choice = "Bao"
    
    # Xử lý khi người chơi đã chọn
    if st.session_state.player_choice:
        # Máy chọn ngẫu nhiên
        choices = ["Kéo", "Búa", "Bao"]
        st.session_state.computer_choice = random.choice(choices)
        
        # Hiển thị lựa chọn
        st.write(f"Bạn chọn: {st.session_state.player_choice}")
        st.write(f"Máy chọn: {st.session_state.computer_choice}")
        
        # Xác định kết quả
        st.session_state.result = determine_winner(st.session_state.player_choice, st.session_state.computer_choice)
        st.write(st.session_state.result)
        
        # Nút chơi lại
        if st.button("Chơi lại"):
            st.session_state.player_choice = None
            st.session_state.computer_choice = None
            st.session_state.result = ""

# Chạy trò chơi
render_game()
