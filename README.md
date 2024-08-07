AI Podcast Research Helper
Overview
The AI Podcast Research Helper is designed to streamline the guest research process for podcasters. By leveraging powerful tools such as Streamlit for the user interface, DuckDuckGo Search for gathering data, and the Falcon Model from AI71 for summarizing information, this application provides podcasters with a comprehensive and efficient way to gather detailed information about their guests.

Features
Automated Research: Fetches relevant guest information using DuckDuckGo Search.
Information Summarization: Uses the Falcon Model from AI71 to summarize collected data.
Easy-to-Use Interface: Built with Streamlit for a seamless user experience.
Multimedia Integration: Retrieves images and videos related to the guest.
Custom Question Generation: Generates tailored questions based on guest details and audience type.


You can install the required packages using:
pip install -r requirements.txt

Set Up Environment Variables:
Add your AI71 API key in the .env file:
AI71_API_KEY=your_api_key_here

Create secrets.toml file in .streamlit
Add your AI71 API key in the secrets.toml file:
AI71_API_KEY=your_api_key_here

Run the Streamlit App:
streamlit run app.py
