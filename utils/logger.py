from datetime import datetime
import json
import platform
import uuid
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
from typing import Any


class FirestoreLogger:
    def __init__(self):
        # Check if Firebase has already been initialized
        try:
            firebase_admin.get_app()
        except ValueError:
            # If not, initialize it
            encoded_credentials = st.secrets["ENCODED_CREDS"]
            decoded_credentials = base64.b64decode(
                encoded_credentials).decode()
            credentials_json = json.loads(decoded_credentials)
            cred = credentials.Certificate(credentials_json)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def to_firestore(self, objective: Any, hate_flag: bool, sexual_flag: bool) -> None:
        """
        Uploads the given flags along with a unique identifier and system info to Firestore.

        Parameters:
        objective (Any): The main objective of the call.
        hate_flag (bool): A flag indicating a hate speech identifier.
        sexual_flag (bool): A flag indicating a sexual content identifier.

        Returns:
        None
        """
        unique_id = str(uuid.uuid4())  # Generate a unique identifier
        doc_ref = self.db.collection('user_prompts').document(unique_id)
        doc_ref.set({
            'objective': objective,
            'hate_flag': hate_flag,
            'sexual_flag': sexual_flag,
            'timestamp': datetime.utcnow().isoformat(),
            'user_agent': platform.platform()
        })
