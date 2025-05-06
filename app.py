import streamlit as st
from PIL import Image, UnidentifiedImageError
import io

st.set_page_config(page_title="Chuyển ảnh sang file .ico", layout="centered")
st.title("🖼️ Chuyển đổi ảnh PNG/JPG thành file ICO")

uploaded_file = st.file_uploader("📤 Tải ảnh lên (.png hoặc .jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Đọc ảnh từ file upload
        image = Image.open(uploaded_file).convert("RGBA")

        # Hiển thị ảnh (sử dụng use_column_width để tương thích rộng nhất)
        st.image(image, caption="Ảnh đã tải lên", use_column_width=True)

        # Tạo kích thước icon tiêu chuẩn
        icon_size = (256, 256)
        resized_image = image.resize(icon_size)

        # Tạo file .ico trong bộ nhớ
        ico_bytes = io.BytesIO()
        resized_image.save(ico_bytes, format='ICO')
        ico_bytes.seek(0)

        # Hiển thị nút tải xuống
        st.success("✅ Đã chuyển đổi thành công!")
        st.download_button(
            label="⬇️ Tải file icon.ico",
            data=ico_bytes,
            file_name="icon.ico",
            mime="image/x-icon"
        )

    except UnidentifiedImageError:
        st.error("❌ File bạn tải lên không phải ảnh hợp lệ.")
    except Exception as e:
        st.error(f"❌ Lỗi xử lý: {e}")
