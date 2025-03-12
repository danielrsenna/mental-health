import functools
import os

import reflex as rx

from mental_health.states.auth import AuthState
from mental_health.ui import navbar, google_auth_buttom
from mental_health.ui.google_login_buttom import GoogleOAuthProvider


def loginpage() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar(),
        _login_section(),
        #footer(),
        direction="column",
        justify="center",
        align="center",
        background_color="#ffffff",
        height="100vh",
    )


def _login_section() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src="/sloth_logo_white.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Acesse a sua conta",
                        size="6",
                        as_="h2",
                        text_align="left",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.text(
                            "Não tem conta?",
                            size="3",
                            text_align="left",
                        ),
                        rx.link("Criar", href="#", size="3"),
                        spacing="2",
                        opacity="0.8",
                        width="100%",
                    ),
                    direction="column",
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Senha",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Esqueci minha senha",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Digite a sua senha",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Entrar", size="3", width="100%", background_color=rx.color("gray", 12)),
                rx.hstack(
                    rx.divider(margin="0"),
                    rx.text(
                        "Ou continue com",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    rx.divider(margin="0"),
                    align="center",
                    width="100%",
                ),
                google_auth_buttom(),
                spacing="6",
                width="100%",
                align="center",
            ),
            size="4",
            max_width="28em",
            width="100%",
        ),
        spacing="2",
        direction="column",
        height="100vh",
        width="100vw",
        justify="center",
        align="center",
        #padding="5em",
    )


def require_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(AuthState.is_hydrated,
                rx.cond(AuthState.is_token_valid,
                    page(),
                    loginpage()
                ),
                rx.spinner(),
            ),
            client_id=os.environ['GOOGLE_CLIENT_ID'],
        )

    return _auth_wrapper
