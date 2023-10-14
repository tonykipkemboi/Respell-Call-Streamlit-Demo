# Respell Call Streamlit App 📞

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://respellcall.streamlit.app/)

Ring, Ring, who's calling? ☎️

Check out how I gave myself a ring using this app! 📞🤙

![Conversation Catalyst](assets/respell.gif)

Welcome to the `Respell Call Streamlit App`, your gateway to initiating calls with a sprinkle of awesomeness. Let's cut to the chase and dive right in, shall we?

## What's this all about? 🤔

This Streamlit app is your virtual assistant, making calls to the phone number you provide and carrying out the objective you set.

## Features 🫠

- **`User-Friendly Interface`**: [Streamlit](https://www.streamlit.io) UI which makes building Python apps easy-peasy lemon squeezy!

- **`Secure API Calls`**: Utilizes the Respell API for secure and efficient calls.

- **`Content Moderation`**: Uses [Lakera AI](https://lakera.ai/) for real-time prompt moderation to keep the conversation clean and respectful.

- **`Interactive Chat Transcript`**: You get a neat transcript of your call, so you can analyze all the little details afterwards.

## How to Get Started 🎉

1. Clone the repository:

   ```bash
   git clone https://github.com/tonykipkemboi/Respell-Call-Streamlit-Demo.git
   ```

2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your API keys to a secrets.toml file in the root directory of this project. Streamlit will pick it up automatically when you run the app.

   Here's how your **`secrets.toml`** file should look like:

   ```TOML
   [default]
   RESPELL_API = "your-respell-api-key-goes-here"
   SPELL_ID = "your-spell-id-goes-here"
   SPELL_VERSION = "your-spell-version-goes-here"
   LAKERA_API_KEY = "your-lakera-api-key-goes-here"
   ```

4. Run the App - In your terminal, navigate to the folder where the app is located and type:

   ```bash
   streamlit run streamlit_app.py
   ```

5. Enjoy! - Play around with the app, and don't forget to wear a smile!

## Behind the Scenes 🧙🏽‍♂️

- **`parse_transcript Function`**: This function takes the transcript text, splits it into separate messages, and filters out the unwanted substrings, giving you a clean and structured output.

- **`Moderation with Lakera`**: Before making a call, the objective (prompt) text is sent to Lakera for moderation. If it contains hate speech or sexual content, the call won't proceed. So, keep it classy!

- **`Session State`**: We use the session state to hold onto your messages throughout your session.

## This Streamlit app is powered by 🔋

[![Conversation Catalyst](assets/respell_logo.svg)](https://www.respell.ai/)

[![Conversation Catalyst](assets/lakera.svg)](https://www.lakera.ai/)
