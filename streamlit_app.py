import streamlit as st
import requests
import json
import re

from typing import List, Dict, Union

# ------------------ Configuration and UI setup -------------------

st.set_page_config(
    page_title="Respell Call Streamlit App",
    page_icon="📞",
    layout="centered",
)

# Logo and brand display
st.markdown(
    """
    <a href="https://www.respell.ai/" target="_blank">
        <svg width="301" height="70" viewBox="3 0 106 26" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M22.057 10.84C22.057 5.12938 17.3784 0.5 11.607 0.5C8.52934 0.5 5.7624 1.81648 3.85 3.91138L2.13975 5.89C0.797345 7.62931 0 9.80252 0 12.16C0 17.8706 4.67862 22.5 10.45 22.5C13.4392 22.5 16.1353 21.2581 18.04 19.2673L19.7427 17.33C21.1903 15.5556 22.057 13.298 22.057 10.84ZM20.68 10.84C20.68 15.8085 16.6056 19.86 11.55 19.86C6.49444 19.86 2.42 15.8085 2.42 10.84C2.42 5.87153 6.49444 1.82 11.55 1.82C16.6056 1.82 20.68 5.87153 20.68 10.84ZM12.124 5.21848C12.0145 4.79384 11.4114 4.79384 11.3019 5.21848C10.6844 7.61221 8.81517 9.48145 6.42144 10.0989C5.9968 10.2085 5.9968 10.8115 6.42144 10.9211C8.81517 11.5385 10.6844 13.4078 11.3019 15.8015C11.4114 16.2262 12.0145 16.2262 12.124 15.8015C12.7415 13.4078 14.6107 11.5385 17.0045 10.9211C17.4291 10.8115 17.4291 10.2085 17.0045 10.0989C14.6107 9.48145 12.7415 7.61221 12.124 5.21848Z" fill="#6A5CFF"/>
        <path d="M37.5448 13.8137L41.0121 20.4998H38.3241L35.0262 14.1299H31.1749V20.4998H28.8145V4.23628H35.3876C35.7039 4.23628 36.2121 4.25887 36.6413 4.32664C39.3632 4.74452 40.7185 6.6984 40.7185 9.18311C40.7185 11.1031 39.6568 13.0796 37.5448 13.8137ZM35.2973 6.46123H31.1749V11.905H35.2973C35.5909 11.905 36.0088 11.905 36.325 11.792C37.7707 11.2951 38.3128 10.2335 38.3128 9.18311C38.3128 8.13275 37.7707 6.91299 36.325 6.57417C35.9862 6.48381 35.5909 6.46123 35.2973 6.46123Z" fill="#6A5CFF"/>
        <path d="M53.3202 15.0673H44.2285C44.4205 17.3375 45.6176 18.6137 47.6732 18.6137C49.1414 18.6137 50.2482 17.9248 50.8468 16.6711L53.1621 17.4052C52.2134 19.585 50.1466 20.8386 47.7861 20.8386C44.1381 20.8386 41.6986 18.2749 41.6986 14.5026C41.6986 10.5045 44.1042 7.96334 47.6732 7.96334C51.4002 7.96334 53.5687 10.6965 53.3202 15.0673ZM47.7635 10.0528C45.7532 10.0528 44.5899 11.1596 44.2849 13.2264H50.9033C50.6548 11.0692 49.6383 10.0528 47.7635 10.0528Z" fill="#6A5CFF"/>
        <path d="M59.3892 20.8273C56.4189 20.8273 54.465 19.4608 54.0471 17.0777L56.464 16.705C56.769 17.9812 57.921 18.7492 59.5473 18.7492C61.0156 18.7492 61.9078 18.1168 61.9078 17.0551C61.9078 16.129 61.5012 15.8805 58.6325 15.1125C55.4815 14.288 54.4424 13.4184 54.4424 11.6226C54.4424 9.40899 56.3172 7.96334 59.1859 7.96334C61.9869 7.96334 63.9972 9.37511 64.2683 11.5436L61.8513 11.984C61.6819 10.8208 60.6993 10.0979 59.2085 10.0415C57.7742 9.98499 56.8029 10.5723 56.8029 11.4984C56.8029 12.3116 57.3563 12.6278 60.2137 13.3506C63.2857 14.1412 64.336 15.0786 64.336 16.9648C64.336 19.3817 62.4725 20.8273 59.3892 20.8273Z" fill="#6A5CFF"/>
        <path d="M71.3866 7.96334C74.82 7.96334 76.9546 10.7078 76.9546 14.3897C76.9546 18.049 74.8313 20.8386 71.4317 20.8386C70.0426 20.8386 68.9244 20.3982 68.0661 19.6415V25.921H65.6943V8.30217H67.795V9.3977C68.6647 8.49417 69.8732 7.96334 71.3866 7.96334ZM71.1042 18.704C73.3743 18.704 74.4473 16.8066 74.4473 14.3897C74.4473 11.9953 73.3743 10.0979 71.0252 10.0979C68.8002 10.0979 67.795 11.8598 67.795 14.3897C67.795 16.9196 68.7776 18.704 71.1042 18.704Z" fill="#6A5CFF"/>
        <path d="M89.2629 15.0673H80.1711C80.3631 17.3375 81.5603 18.6137 83.6158 18.6137C85.084 18.6137 86.1909 17.9248 86.7895 16.6711L89.1047 17.4052C88.156 19.585 86.0892 20.8386 83.7287 20.8386C80.0807 20.8386 77.6412 18.2749 77.6412 14.5026C77.6412 10.5045 80.0469 7.96334 83.6158 7.96334C87.3429 7.96334 89.5113 10.6965 89.2629 15.0673ZM83.7062 10.0528C81.6958 10.0528 80.5325 11.1596 80.2276 13.2264H86.8459C86.5975 11.0692 85.581 10.0528 83.7062 10.0528Z" fill="#6A5CFF"/>
        <path d="M93.2537 20.4998H90.8933V3.89746H93.2537V20.4998Z" fill="#6A5CFF"/>
        <path d="M98.1023 20.4998H95.7418V3.89746H98.1023V20.4998Z" fill="#6A5CFF"/>
        </svg>
    </a>
    """,
    unsafe_allow_html=True,
)

st.caption(
    "Makes a call to the phone number provided and carries out the objective!")
with st.expander(":blue[**Inspiring Example by [@harpriiya](https://x.com/harpriiya?s=20)**]"):
    st.markdown(
        """
        <iframe src="https://twitframe.com/show?url=https://twitter.com/harpriiya/status/1682165101867175936" 
                width="650" 
                height="795" 
                frameborder="0" 
                scrolling="no">
        </iframe>
        """,
        unsafe_allow_html=True,
    )
st.divider()


# ------------------ API and Secret Keys -------------------------

RESPELL_API = st.secrets["RESPELL_API"]
SPELL_ID = st.secrets["SPELL_ID"]
SPELL_VERSION = st.secrets["SPELL_VERSION"]
LAKERA_GUARD_ACCESS_KEY = st.secrets["LAKERA_API_KEY"]

# --------------- Parsing and Transcript Logic --------------------


def parse_transcript(transcript_text: str) -> List[Dict[str, Union[str, str]]]:
    """Parse the transcript text into structured messages."""
    messages = transcript_text.split('\n')
    structured_messages = []
    for msg in messages:
        # Find the role and content of the message using regex
        match = re.match(r'(Assistant|User): (.*)', msg)
        if match:
            role, content = match.groups()
            # Filtering out unwanted substrings
            if "action:" not in content and "Finish FINISH" not in content:
                structured_messages.append(
                    {"role": role.lower(), "content": content.strip()})

    return structured_messages


# --------------- Initialize and Handle Session State ------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ User Input and API Calls --------------------

with st.form("my_form"):
    st.subheader(":blue[Initiate a Call]", anchor=False)
    st.caption("Call transcript will be displayed below after the call.")
    phone_number = st.text_input(
        "**Phone Number**", placeholder="📞 (123) 456-7890", help="Enter the phone number you want to call.", type="password")
    objective = st.text_area(
        "**Objective**", placeholder="Type here...", help="Specify the objective of the call.")
    # Submit inputs
    submitted = st.form_submit_button(
        ":blue[▶️ Call]", use_container_width=True)
    st.caption(
        "*️⃣ Next app update will be to make the transcript streaming...")

if submitted:
    try:
        # Moderation check using Lakera AI API
        # do not send to Respell if prompt contains hate or sexual content
        moderation = requests.post(
            "https://api.lakera.ai/v1/moderation",
            json={"input": objective},
            headers={"Authorization": f"Bearer {LAKERA_GUARD_ACCESS_KEY}"},
        )
        lakera_response = moderation.json()
        hate_flag = lakera_response['results'][0]['categories']['hate']
        sexual_flag = lakera_response['results'][0]['categories']['sexual']

        if not (hate_flag or sexual_flag):
            # Make the API call
            response = requests.post(
                "https://api.respell.ai/v1/run",
                headers={
                    # This is your API key
                    "Authorization": RESPELL_API,
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "spellId": SPELL_ID,
                    "spellVersionId": SPELL_VERSION,
                    "inputs": {
                        "phone_number": phone_number,
                        "objective": objective,
                    }
                })
            )
            # Process and display the transcript
            response_data = response.json()
            transcript_output = response_data.get('outputs', {}).get(
                'output', 'No transcript available')
            structured_messages = parse_transcript(transcript_output)
            st.session_state.messages.extend(structured_messages)

            # Display all messages from the session state
            st.subheader(":blue[Call Transcript]")
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
        else:
            if hate_flag and sexual_flag:
                st.warning(":red[Whoa there, your prompt contains both hate speech and sexual language. Let's keep it clean.]",
                           icon="⛔️")
                st.stop()
            elif hate_flag:
                st.warning(
                    ":red[Hold up! Your prompt contains hate speech. Let's be nice.]", icon="🙅🏽‍♂️")
                st.stop()
            elif sexual_flag:
                st.warning(
                    ":red[Uh-oh, looks like your prompt has sexual language. Clean it up, please.]", icon="🔞")
                st.stop()

    except Exception as e:
        st.error(f"An error has occured: {e}", icon="🚨")
else:
    st.warning("Enter phone number and objective to make a call.", icon="⚠️")

# ------------------ Credits --------------------

st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: small;'>
        Made with 💙 by <a href='https://twitter.com/tonykipkemboi' target='_blank'>@tonykipkemboi</a> 
        | Find me on <a href='https://linkedin.com/in/tonykipkemboi' target='_blank'>LinkedIn</a>
        | Check out & ⭐️ <a href='https://github.com/tonykipkemboi/Respell-Call-Streamlit-Demo.git' target='_blank'>GitHub Repo</a>
    </p>
    """,
    unsafe_allow_html=True,
)
