import os

from mental_health.states.auth import AuthState

import reflex as rx


class GoogleOAuthProvider(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleOAuthProvider"

    client_id: rx.Var[str]


class GoogleLogin(rx.Component):
    library = "@react-oauth/google"
    tag = "GoogleLogin"

    on_success: rx.EventHandler[lambda data: [data]]


def authpage() -> rx.Component:
    return rx.vstack(
        GoogleOAuthProvider.create(
            GoogleLogin.create(on_success=AuthState.on_success),
            client_id=os.environ['GOOGLE_CLIENT_ID'],
        )
    )
