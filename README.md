# Respell Call Streamlit App 📞

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://respellcall.streamlit.app/)

Hey there, code explorer!👋🏾

![Conversation Catalyst](assets/phone.png)

Welcome to the `Respell Call Streamlit App`, your gateway to initiating calls with a sprinkle of awesomeness. Let's cut to the chase and dive right in, shall we?

## What's this all about? 🤔

This Streamlit app is your virtual assistant, making calls to the phone number you provide and carrying out the objective you set.

## Features 🫠

- **`User-Friendly Interface`**: Easy-peasy lemon squeezy! Just follow the instructions and you'll be on your way.

- **`Secure API Calls`**: Utilizes the Respell API for secure and efficient calls.

- **`Interactive Chat Transcript`**: You get a neat transcript of your call, so you can analyze all the little details afterwards.

## How to Get This Party Started 🎉

1. Clone the repository:

   ```bash
   git clone https://github.com/tonykipkemboi/Respell-Call-Streamlit-Demo.git
   ```

2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the App - In your terminal, navigate to the folder where the app is located and type:

   ```bash
   streamlit run streamlit_app.py
   ```

4. Enjoy! - Play around with the app, and don't forget to wear a smile!

## Behind the Scenes 🧙🏽‍♂️

- **`parse_transcript Function`**: This function takes the transcript text, splits it into separate messages, and filters out the unwanted substrings, giving you a clean and structured output.
- **`Session State`**: We use the session state to hold onto your messages throughout your session.

This Streamlit app is powered by:

[![Conversation Catalyst](assets/respell_logo.svg)](https://www.respell.ai/)
