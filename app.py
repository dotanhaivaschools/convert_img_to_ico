import streamlit as st
from PIL import Image, UnidentifiedImageError
import io

st.set_page_config(page_title="Chuyển ảnh sang file .ico", layout="centered")
st.title("🖼️ Chuyển đổi ảnh PNG/JPG thành file ICO")

uploaded_file = st.file_uploader("📤 Tải ảnh lên (.png hoặc .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGBA")
        st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

        icon_size = (256, 256)
        resized_image = image.resize(icon_size)

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
    except UnidentifiedImageError:
        st.error("❌ Không thể đọc ảnh. Vui lòng đảm bảo file là ảnh PNG hoặc JPG hợp lệ.")
    except Exception as e:
        st.error(f"❌ Lỗi khi xử lý ảnh: {e}")
