
import streamlit as st

# Cấu hình người dùng mẫu
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "123456"
}

# Tiêu đề
st.title("🔐 Trang Đăng Nhập với Streamlit")

# Giao diện nhập liệu
username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

# Xử lý đăng nhập
if st.button("Đăng nhập"):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.success(f"✅ Đăng nhập thành công! Xin chào, {username}!")
    else:
        st.error("❌ Sai tên đăng nhập hoặc mật khẩu!")
