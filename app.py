import streamlit as st
import os
import time
from ransomware_core import *
import feedparser
from datetime import datetime

def fetch_ransomware_news():
    FEEDS = {
        "🧠 The Hacker News": "https://thehackernews.com/rss",
        "📊 Rapid7": "https://blog.rapid7.com/rss/",
        "🗞️ ThreatPost": "https://threatpost.com/feed/",
        "🔐 Kaspersky SecureList": "https://securelist.com/feed/",
    }

    for name, url in FEEDS.items():
        feed = feedparser.parse(url)
        st.markdown(f"#### {name}")
        count = 0
        for entry in feed.entries:
            if "ransomware" in entry.title.lower() or "ransomware" in entry.summary.lower():
                st.markdown(f"🔸 **[{entry.title}]({entry.link})**")
                count += 1
                if count >= 3:
                    break
        if count == 0:
            st.markdown("✅ No ransomware-specific articles today.")

st.title("🔒 RansomSim: Ransomware Attack Simulator")

folder = st.text_input("📂 Enter folder path to simulate attack")

all_types = [
    ".txt", ".pdf", ".docx", ".jpg", ".png", ".csv", ".xlsx",
    ".pptx", ".mp3", ".mp4", ".json", ".xml", ".html", ".css", ".js"
]
if st.checkbox("Select all file types"):
    file_types = all_types
else:
    file_types = st.multiselect("Filter by file types to encrypt", all_types, default=[".txt", ".jpg", ".pdf"])

log_lines = []

if folder and os.path.isdir(folder):
    files = list_target_files(folder, file_types)
    st.write(f"Found `{len(files)}` target file(s)")

    if st.button("🔐 Encrypt Files"):
        if not os.path.exists("secret.key"):
            generate_key()
        key = load_key()

        progress = st.progress(0)
        for i, file in enumerate(files):
            encrypt_file(file, key)
            log_lines.append(f"[{datetime.now().strftime('%H:%M:%S')}] Encrypted {os.path.basename(file)}")
            progress.progress((i + 1) / len(files))
            time.sleep(0.1)
        st.error("💰 All your files have been encrypted! This is a simulation.")

    if st.button("🔓 Decrypt Files"):
        if not os.path.exists("secret.key"):
            st.warning("No key found.")
        else:
            key = load_key()
            progress = st.progress(0)
            for i, file in enumerate(files):
                success = decrypt_file(file, key)
                log = f"[{datetime.now().strftime('%H:%M:%S')}] Decrypted {os.path.basename(file)}" if success else "❌ Failed"
                log_lines.append(log)
                progress.progress((i + 1) / len(files))
                time.sleep(0.1)
            st.success("✅ Files decrypted (if key matched)")

    with st.expander("📜 Terminal Log"):
        for log in log_lines:
            st.text(log)

    with st.expander("📡 Live Ransomware News & Tips"):
        fetch_ransomware_news()
else:
    st.warning("Enter a valid folder path on your local machine.")