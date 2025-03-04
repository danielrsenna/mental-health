import reflex as rx
import uuid

from mental_health.services.gpt_client import GptClient
from mental_health.services.db_client import DatabaseClient
from mental_health.models import Message


def _stripe_chat_history(chat_history):
    return '\n'.join(
        f'Q: {question}\nA: {answer}\n'
        for question, answer in chat_history
    )


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        chat_bot_client = GptClient()

        answer = ''
        self.chat_history.append((self.question, answer))

        # clear the prompt input
        self.question = ''
        yield

        async for answer in chat_bot_client.answer(_stripe_chat_history(self.chat_history)):
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer,
            )
            yield

        db_client = DatabaseClient(model='mongodb')
        db_client.insert(Message(
            user_id=uuid.uuid4(),
            content=f'User: {self.chat_history[-1][0]}\nBot: {self.chat_history[-1][1]}',
            session_id=uuid.uuid4(),
            prompt_id=uuid.uuid4(),
        ))
