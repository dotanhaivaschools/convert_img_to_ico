import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Chuyển ảnh sang file .ico", layout="centered")
st.title("🖼️ Chuyển đổi ảnh PNG/JPG thành file ICO")

uploaded_file = st.file_uploader("📤 Tải ảnh lên (.png hoặc .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGBA")
    
    # ✅ Dùng use_container_width thay cho use_column_width
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)
    
    # Resize ảnh về kích thước 256x256
    icon_size = (256, 256)
    resized_image = image.resize(icon_size)

    # Chuyển ảnh thành định dạng .ico trong bộ nhớ
    ico_bytes = io.BytesIO()
    resized_image.save(ico_bytes, format='ICO')
    ico_bytes.seek(0)

    st.success("✅ Đã chuyển đổi thành công!")
    st.download_button(
        label="⬇️ Tải file .ico",
        data=ico_bytes,
        file_name="icon.ico",
        mime="image/x-icon"
    )
