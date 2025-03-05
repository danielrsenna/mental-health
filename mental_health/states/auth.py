import os

from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import reflex as rx

class AuthState(rx.State):

    def on_success(self, id_token: dict):
        verify_oauth2_token(
            id_token["credential"],
            requests.Request(),
            os.environ["GOOGLE_CLIENT_ID"],
        )
