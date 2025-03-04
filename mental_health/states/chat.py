import os

import dotenv
import reflex as rx

from mental_health.services.gpt_client import GptClient


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        dotenv.load_dotenv()

        client = GptClient()

        answer = ''
        self.chat_history.append((self.question, answer))

        async for answer in client.answer(self.question):
            if self.question:
                self.question = ''
                yield
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer,
            )
            yield
