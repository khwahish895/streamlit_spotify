# mood_music_app.py
import streamlit as st
import webbrowser
import google.generativeai as genai

# 🔑 Set your Gemini API Key
genai.configure(api_key="AIzaSyDrx7j5XPIztMz274t-ItjxSE55sr6Q39g")

# Define mood-to-Spotify mapping
mood_to_spotify = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DWY3PJWG3ogmJ",
    "relaxed": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
    "romantic": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn",
    "motivated": "https://open.spotify.com/playlist/37i9dQZF1DX1s9knjP51Oa"
}

# 🎵 Gemini: Detect mood
def detect_mood(text):
    prompt = f"What is the emotional mood in this text: '{text}'? Respond with one word like happy, sad, angry, relaxed, romantic, or motivated."
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    mood = response.text.strip().lower()
    return mood

# 🎯 Streamlit UI
st.set_page_config(page_title="🎧 Mood Music Recommender", layout="centered")
st.title("🎵 Mood-Based Spotify Recommender")

user_input = st.text_area("Describe your current mood or feeling:")

if st.button("🎶 Recommend a Song"):
    if user_input.strip() == "":
        st.warning("Please describe how you're feeling.")
    else:
        mood = detect_mood(user_input)
        st.write(f"**Detected Mood:** `{mood}`")

        if mood in mood_to_spotify:
            spotify_url = mood_to_spotify[mood]
            st.success(f"Here's a song/playlist for your mood: **{mood.capitalize()}**")
            st.markdown(f"[▶️ Open in Spotify]({spotify_url})", unsafe_allow_html=True)
            webbrowser.open(spotify_url)
        else:
            st.error("Sorry, I couldn't match your mood to a playlist. Try using simpler descriptions.")
