import streamlit as st
import uvicorn # type: ignore
import string
from collections import Counter

# Streamlit UI
st.title("Text Analyzer App")
st.write("Analyze word count, character count, and most common words.")

# Text Input
user_text = st.text_area("Enter your text here:", height=200)

if user_text:
    # Word and Character Count
    word_count = len(user_text.split())
    char_count = len(user_text)
    st.write(f"Word Count: {word_count}")
    st.write(f"Character Count: {char_count}")
    
    # Most Common Words
    words = user_text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    common_words = Counter(words).most_common(5)
    st.write("Most Common Words:")
    st.write(common_words)
    
    # Download Processed Data
    if st.button("Download Analysis Report"):
        report = f"Word Count: {word_count}\nCharacter Count: {char_count}\nMost Common Words: {common_words}"
        st.download_button("Download Report", report, "text_analysis.txt", "text/plain")

# Run the app with UVicorn
if __name__ == "__main__":
    uvicorn.run("text_analyzer:app", host="0.0.0.0", port=8502, reload=False)
