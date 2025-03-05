import reflex as rx
import uuid

from mental_health.models.message import BOT_USER_ID
from mental_health.models.session import Session
from mental_health.services.gpt_client import GptClient
from mental_health.services.db_client import DatabaseClient
from mental_health.models import Message

class ChatState(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    # The current user's ID.
    _user_id: str

    # The current session ID.
    _session_id: str

    @rx.event
    def on_load(self):
        self._start_new_session()

    async def answer(self):
        chat_bot_client = GptClient()

        self.chat_history.append((self.question, ""))

        # clear user input
        user_question = self.question
        self.question = ''
        yield

        answer = await chat_bot_client.answer(self.chat_history, user_question)

        self.chat_history[-1] = (self.chat_history[-1][0], answer)
        yield

        db_client = DatabaseClient(model='mongodb')

        question, answer = self.chat_history[-1]
        db_client.table('messages').insert(
            Message(
                user_id=self._user_id,
                content=question,
                session_id=self._session_id,
        )).insert(
            Message(
                user_id=BOT_USER_ID,
                content=answer,
                session_id=self._session_id,
        ))

    def _start_new_session(self):
        self._user_id = str(uuid.uuid4())
        self._session_id = str(uuid.uuid4())
        DatabaseClient(model='mongodb').table('sessions').insert(Session(uuid=self._session_id))
        self.chat_history = []
