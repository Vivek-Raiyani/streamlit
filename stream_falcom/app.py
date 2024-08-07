import streamlit as st
from duckduckgo_search import DDGS
from ai71 import AI71
import os
from dotenv import load_dotenv

load_dotenv()

def get_image_url(name):
    images = DDGS().images(name, max_results=1)
    if images:
        return images[0]['image']
    return None

def get_video_url(name):
    videos = DDGS().videos(f"podcast featuring {name} on youtube , dont look for other platform", max_results=3)  # Assuming this function returns video URLs
    if videos:
        return [video['content'] for video in videos]  # Adjust based on actual structure
    return []

def get_social_media_links(name):
    social_media_links = DDGS().chat(f"social media account links: {name}")
    if social_media_links:
        return social_media_links
    return []

def get_guest_details(name):
    guest_details = DDGS().chat(f" give me a summary :{name} biography,careers, journey, milestones achieved,etc")
    if guest_details:
        return guest_details
    return []

def get_guest_ventures(name):
    guest_ventures = DDGS().chat(f"businees/organizations {name} is part of , give me only names and the role of guest ")
    if guest_ventures:
        return guest_ventures
    return []

def generate_questions(name,audience_type):
          system=f'''
                    Help us understand the guest of our podcast.
                    You will be provided with the details of the guest of our podcast and the type of audience of our podcast.
                    you need to do a summary of the guest of our podcast , and suggest questions for our guest  considering the audience of our podcast and the guest .
                    you need to come up with  3 questions that will help us understand the guest of our podcast.
                    you need to come up with  3 questions each related to their journey, industry, and business they are invloed.
                    You need to come up with  3 questions about the problems they are facing in their journey, life, career, etc.
                    lastly you need to come up with 3 question our audience is looking for from our guest.

                    in your resonse only include the question and the point of time of where it needs to be asked.

                    Audience type of our podcast : {audience_type}
'''

          client = AI71(st.secrets["AI71_API_KEY"])
          
          questions = ''
          for details in [get_guest_details(name),get_guest_ventures(name)]:
                    response=client.chat.completions.create(
                    model="tiiuae/falcon-180B-chat",
                    messages=[
                              {"role": "system", "content": system}, {"role": "user", "content": "Guest name : "},
                              {"role": "user", "content": details},
                    ],
                    temperature=0.9,
                    ).choices[0].message.content
                    questions+=response+'\n'
          return questions          





def display_home_page():
    st.title("Podcast_Research App")
    st.session_state.name = st.text_input("Enter your name", "")
    st.session_state.email = st.text_input("Enter your email", "")
    st.session_state.podcast = st.text_input("Enter your podcast name", "")
    st.session_state.guest_name = st.text_input("Guest name", "")
    st.session_state.audience_type = st.text_area("Enter your audience type", "")

    submit = st.button("Submit")

    if submit:
        if not st.session_state.name or not st.session_state.email or not st.session_state.podcast or not st.session_state.guest_name or not st.session_state.audience_type:
            st.error("All fields are required.")
        else:
            st.session_state.page = "research"
            st.rerun()

def display_research_page():
    st.title("Guest_Research")

    guest_image_url = get_image_url(st.session_state.guest_name)  # Ensure this function returns a list with 'image' keys
    if guest_image_url:
          st.header(st.session_state.guest_name)
          st.image(guest_image_url)

    st.write("links")
            #st.logo(link=url,image="images/hero.jpg")
    st.subheader("biography")
    st.write(get_guest_details(st.session_state.guest_name))
    st.write(get_guest_ventures(st.session_state.guest_name))
    
    # questions
    st.write(generate_questions(st.session_state.guest_name,st.session_state.audience_type))

    for url in get_video_url(st.session_state.guest_name):
        if url:
            st.video(data=url)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Display content based on session state
if st.session_state.page == "home":
    display_home_page()
elif st.session_state.page == "research":
    display_research_page()
else:
    st.write("Page not found")
