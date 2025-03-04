import reflex as rx

from ..ui import sidebar_chat
from ..states.chat import ChatState
from ..styles import chatpage as style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.flex(
        rx.foreach(
            ChatState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        width="40vw",
        direction="column",
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatState.question,
            placeholder="Converse com Kuatan",
            on_change=ChatState.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Enviar",
            on_click=ChatState.answer,
            style=style.button_style,
        ),
    )

def main_section() -> rx.Component:
    return rx.flex(
        chat(),
        action_bar(),
        align='center',
        direction="column",
        justify='end',
        #background_color=rx.color("gray", 5),
        width="100vw",
        padding="3em",
    )

def chatpage() -> rx.Component:
    return rx.flex(
        sidebar_chat(),
        rx.divider(orientation="vertical"),
        main_section(),
        direction="row",
        height="100vh",
        width="100vw",
    )
