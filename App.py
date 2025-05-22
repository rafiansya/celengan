import streamlit as st
from PIL import Image
import os

st.title("Anime Viewer")

# Path folder anime (pastikan sesuai dengan struktur repo kamu)
anime_folder = "anime"

# Ambil semua file gambar/gif di folder anime
anime_files = [f for f in os.listdir(anime_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Dropdown untuk memilih anime
selected = st.selectbox("Pilih anime:", anime_files)

# Tampilkan anime
file_path = os.path.join(anime_folder, selected)
if selected.endswith('.gif'):
    st.image(file_path, caption=selected)
else:
    img = Image.open(file_path)
    st.image(img, caption=selected)
