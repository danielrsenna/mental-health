import json
import os
import time

from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
import reflex as rx

from mental_health.states import navigation

class AuthState(rx.State):

    # The Google ID token as a JSON string.
    _id_token_json: str = rx.Cookie(
        name='id_token_json',
    )

    def on_success(self, id_token: dict):
        self._id_token_json = json.dumps(id_token)

    @rx.var(cache=True)
    def tokeninfo(self) -> dict[str, str]:
        try:
            return verify_oauth2_token(
                json.loads(self._id_token_json)['credential'],
                requests.Request(),
                os.environ['GOOGLE_CLIENT_ID'],
            )
        except Exception as exc:
            if self._id_token_json:
                print(f'Error verifying token: {exc}')
        return {}

    def logout(self):
        self._id_token_json = ''

    @rx.var
    def is_token_valid(self) -> bool:
        if self.tokeninfo:
            return self.tokeninfo.get('exp', 0.0) > time.time()
        return False

    @rx.event
    def require_auth(self):
        if not self.is_token_valid:
            return rx.redirect(navigation.LOGIN_ROUTE)
