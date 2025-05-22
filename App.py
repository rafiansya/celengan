import streamlit as st

st.title("Anime Viewer dari Link")

# Daftar gambar anime dari link internet
anime_links = {
    "Naruto": "https://media.tenor.com/3tXTApJ-BQ0AAAAC/naruto-running.gif",
    "Luffy": "https://media.tenor.com/1hyOpKwJMPgAAAAC/one-piece-luffy.gif",
    "Mikasa": "https://media.tenor.com/6Zw35aMFO3QAAAAC/mikasa-ackerman-attack-on-titan.gif"
}

# Dropdown untuk pilih anime
selected = st.selectbox("Pilih anime:", list(anime_links.keys()))

# Tampilkan gambar dari link
st.image(anime_links[selected], caption=selected)
