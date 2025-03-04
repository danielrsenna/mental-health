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


class ChatState(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    # The user_id is stored in a cookie and is used to identify the user.
    user_id: str = rx.Cookie(
        name='user_id',
        path='/',
        secure=False,
        max_age=60*60 # 1 hour
    )

    # The session_id is stored in a cookie and is used to identify the session.
    session_id: str = rx.Cookie(
        name='session_id',
        path='/',
        secure=False,
        max_age=60*60 # 1 hour
    )

    def on_load(self):
        if not self.user_id:
            self.user_id = str(uuid.uuid4())

        if not self.session_id:
            self.session_id = str(uuid.uuid4())

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
        db_client.table('messages').insert(Message(
            user_id=self.user_id,
            content=f'User: {self.chat_history[-1][0]}\nBot: {self.chat_history[-1][1]}',
            session_id=self.session_id,
        ))
