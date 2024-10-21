import streamlit as st
import yt_dlp as yt

st.title("download helper")

url = st.text_input("Enter the URL of the video you want to download")

# download the highest quality video
options = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s'
}

if url:
    with yt.YoutubeDL(options) as ydl:
        ydl.download([url])

    st.success("Download complete!")