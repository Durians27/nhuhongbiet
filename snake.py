import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import time

# Cấu hình kích thước và tốc độ game
CELL_SIZE = 20
GRID_SIZE = 20
SPEED = 0.1

# Hàm tạo canvas game
def draw_snake_game(snake, food):
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 1)",  # màu nền
        stroke_width=0,
        background_color="white",
        height=CELL_SIZE * GRID_SIZE,
        width=CELL_SIZE * GRID_SIZE,
        drawing_mode="freedraw",
        key="canvas",
        update_streamlit=True,
    )

    # Vẽ rắn
    for segment in snake:
        canvas_result.image.paste((0, 255, 0), [segment[0] * CELL_SIZE, segment[1] * CELL_SIZE,
                                               (segment[0]+1)*CELL_SIZE, (segment[1]+1)*CELL_SIZE])
    # Vẽ mồi
    canvas_result.image.paste((255, 0, 0), [food[0]*CELL_SIZE, food[1]*CELL_SIZE,
                                           (food[0]+1)*CELL_SIZE, (food[1]+1)*CELL_SIZE])
    return canvas_result

# Khởi tạo session state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.direction = "RIGHT"
    st.session_state.running = False

# Tiêu đề
st.title("🐍 Game Con Rắn - Streamlit")

# Điều khiển
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("▶️ Bắt đầu"):
        st.session_state.running = True

# Điều hướng bằng phím ảo
st.markdown("### Điều hướng:")
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"
with col1:
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"
with col3:
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"
with col2:
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"

# Hàm cập nhật vị trí rắn
def move_snake():
    head = st.session_state.snake[0]
    if st.session_state.direction == "UP":
        new_head = (head[0], head[1] - 1)
    elif st.session_state.direction == "DOWN":
        new_head = (head[0], head[1] + 1)
    elif st.session_state.direction == "LEFT":
        new_head = (head[0] - 1, head[1])
    else:
        new_head = (head[0] + 1, head[1])

    # Kiểm tra va chạm
    if (new_head in st.session_state.snake or
        not (0 <= new_head[0] < GRID_SIZE) or
        not (0 <= new_head[1] < GRID_SIZE)):
        st.session_state.running = False
        st.warning("💀 Game Over!")
        return

    st.session_state.snake = [new_head] + st.session_state.snake

    # Ăn mồi
    if new_head == st.session_state.food:
        st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    else:
        st.session_state.snake.pop()

# Vòng lặp game
if st.session_state.running:
    move_snake()
    draw_snake_game(st.session_state.snake, st.session_state.food)
    time.sleep(SPEED)
    st.experimental_rerun()
else:
    draw_snake_game(st.session_state.snake, st.session_state.food)
