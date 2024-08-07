# AI Podcast Research Helper

## Overview

The AI Podcast Research Helper is designed to streamline the guest research process for podcasters. By leveraging powerful tools such as Streamlit for the user interface, DuckDuckGo Search for gathering data, and the Falcon Model from AI71 for summarizing information, this application provides podcasters with a comprehensive and efficient way to gather detailed information about their guests.

## Features

- **Automated Research:** Fetches relevant guest information using DuckDuckGo Search.
- **Information Summarization:** Uses the Falcon Model from AI71 to summarize collected data.
- **Easy-to-Use Interface:** Built with Streamlit for a seamless user experience.
- **Multimedia Integration:** Retrieves images and videos related to the guest.
- **Custom Question Generation:** Generates tailored questions based on guest details and audience type.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/ai-podcast-research-helper.git
    cd ai-podcast-research-helper
    ```

2. **Install Dependencies:**

    Create a `requirements.txt` file with the following content:

    ```plaintext
    duckduckgo-search
    ai71
    streamlit
    python-dotenv
    ```

    Install the required packages using:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**

    - Create a `.env` file in the project directory.
    - Add your AI71 API key in the `.env` file:

    ```plaintext
    AI71_API_KEY=your_api_key_here
    ```

    - Create a `secrets.toml` file in the `.streamlit` directory.
    - Add your AI71 API key in the `secrets.toml` file:

    ```plaintext
    [secrets]
    AI71_API_KEY = "your_api_key_here"
    ```

## Usage

1. **Run the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

2. **Using the App:**

    - Navigate to the home page.
    - Enter your name, email, podcast name, guest name, and audience type.
    - Click on the "Submit" button to start the research process.
    - View the guest's biography, ventures, images, videos, and generated questions on the research page.



