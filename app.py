import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    st.error("Please set your OPENAI_API_KEY in the .env file.")
    st.stop()

st.title("AI Social Media Manager")
st.write("Use AI tools to create content for businesses.")

# Function to generate text
def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Tabs for each feature
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Instagram Post + Caption", "Reels Script", "Content Calendar", "Hashtag Strategy", "Full Strategy Report"])

with tab1:
    st.header("Instagram Post + Caption")
    business = st.text_input("Describe your business:", key="business1")
    if st.button("Generate", key="gen1"):
        if business:
            prompt = f"Generate 3 A/B/C caption variants for an Instagram post for a business: {business}. Also provide a Canva visual tip."
            result = generate_text(prompt)
            st.write(result)
        else:
            st.warning("Please describe your business.")

with tab2:
    st.header("Reels Script")
    topic = st.text_input("Reels topic:", key="topic2")
    if st.button("Generate Script", key="gen2"):
        if topic:
            prompt = f"Create a full script with timestamps for a Reels video on: {topic}. Include CapCut editing notes."
            result = generate_text(prompt)
            st.write(result)
        else:
            st.warning("Please enter a topic.")

with tab3:
    st.header("Content Calendar")
    pillars = st.text_input("Content pillars:", key="pillars3")
    if st.button("Generate Calendar", key="gen3"):
        if pillars:
            prompt = f"Create a multi-week content calendar with pillars: {pillars}, hooks, and visual notes."
            result = generate_text(prompt)
            st.write(result)
        else:
            st.warning("Please enter content pillars.")

with tab4:
    st.header("Hashtag Strategy")
    niche = st.text_input("Your niche:", key="niche4")
    if st.button("Generate Hashtags", key="gen4"):
        if niche:
            prompt = f"Generate 30 hashtags by category (Mega/Large/Medium/Niche) for niche: {niche}. Include branded ideas."
            result = generate_text(prompt)
            st.write(result)
        else:
            st.warning("Please enter your niche.")

with tab5:
    st.header("Full Strategy Report")
    business_desc = st.text_input("Business description:", key="business5")
    if st.button("Generate Report", key="gen5"):
        if business_desc:
            prompt = f"Create a 90-day roadmap with ChatGPT, Canva & CapCut workflow for business: {business_desc}."
            result = generate_text(prompt)
            st.write(result)
        else:
            st.warning("Please describe your business.")