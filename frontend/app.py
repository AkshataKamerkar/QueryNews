import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/summarize_news"

# Streamlit App UI
st.set_page_config(page_title="News Summarizer", layout="wide")

st.title("📢 AI-Powered News Summarizer")
st.markdown("### Get the latest **summarized** news on your selected topic!")

# User Input
topic = st.text_input("Enter the topic:", placeholder="E.g., RAG technology, AI advancements")
date = st.date_input("Select a date:")

# Submit Button
if st.button("Summarize News 📰"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        st.info("⏳ Fetching the latest news summaries...")

        # Sending API request
        response = requests.post(API_URL, json={"topic": topic, "date": str(date)})

        if response.status_code == 200:
            data = response.json()
            summary_data = data.get("summary", {})

            # Extract first 'raw' summary
            first_summary = summary_data.get("raw", "")

            if first_summary:
                st.success("✅ News Summary Generated Successfully!")
                
                # Display the first raw summary properly formatted
                st.markdown("---")  # Separator
                st.markdown("### 📌 **Latest News Summary**")
                st.markdown(f"> {first_summary}")  # Display first summary in blockquote format
                
            else:
                st.warning("⚠️ No news summary available. Try again later.")
        else:
            st.error("🚨 Error fetching news. Please try again later.")
