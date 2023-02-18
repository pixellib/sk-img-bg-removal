from io import BytesIO
import streamlit as st
from PIL import Image
from rembg import remove

st.title("SK-BG Removel Image Apps")

# Upload your Image file
image_upload = st.file_uploader("Upload your image", type=["png", "jpg", "jpeg","tif","bmp","dicom"])

# Convert the image file into BytesIO so we can download it
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# If we've uploaded an image, open it and remove the background!
if image_upload:
    image = Image.open(image_upload)
    fixed = remove(image)
    downloadable_image = convert_image(fixed)
    st.download_button(
        "Download the Bg removed Image", downloadable_image, "fixed.png", "image/png"
    )
