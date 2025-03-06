import os

from cryptography.fernet import Fernet
import dotenv
from supabase import create_client
from pymongo import MongoClient
from pydantic import BaseModel

from mental_health.feature_flags import FeatureFlags
from mental_health.models.message import Message
from mental_health.models.session import Session


dotenv.load_dotenv()

class _SupaBase:

    def __init__(self, url: str, key: str):
        self._client = create_client(url, key)
        self._table = None

    def table(self, table_name: str):
        self._table = self._client.table(table_name)

    def insert(self, data: dict):
        if self._table is None:
            raise ValueError('No table selected.')

        self._table.insert(data).execute()


class _MongoDB:

    def __init__(self, url: str, database_name: str = 'mental_health'):
        self._client = MongoClient(url, uuidRepresentation="standard")[database_name]
        self._collection = None

    def table(self, table_name: str):
        self._collection = self._client[table_name]

    def _insert_many(self, models: list[BaseModel]):
        self._collection.insert_many([model.model_dump() for model in models])

    def _insert_one(self, model: BaseModel):
        self._collection.insert_one(model.model_dump())

    def insert(self, model: BaseModel|list[BaseModel]):
        if self._collection is None:
            raise ValueError('No collection selected.')

        if isinstance(model, list):
            self._insert_many(model)
        else:
            self._insert_one(model)


class DatabaseClient:

    MODELS = {
        'supabase': lambda: _SupaBase(url=os.environ['SUPABASE_URL'], key=os.environ['SUPABASE_KEY']),
        'mongodb': lambda: _MongoDB(url=os.environ['MONGO_URL'])
    }

    def __init__(self, model: str):
        if model not in self.MODELS:
            raise ValueError(f'Model {model} not found.')

        self._client = self.MODELS[model]()

    def save_messages(self, messages: Message|list[Message]):
        if not isinstance(messages, list) or not all(isinstance(message, Message) for message in messages):
            raise TypeError('Expected a list of Message objects.')

        if FeatureFlags.is_message_encryption_enabled():
            for message in messages:
                message.content = \
                    Fernet(os.environ['FERNET_KEY']).encrypt(message.content.encode('utf-8'))

        self._table('messages')._insert(messages)

    def save_message(self, message: Message):
        if not isinstance(message, Message):
            raise TypeError('Expected a Message object.')

        if FeatureFlags.is_message_encryption_enabled():
            message.content = \
                Fernet(os.environ['FERNET_KEY']).encrypt(message.content.encode('utf-8'))

        self._table('messages')._insert(message)

    def save_session(self, session: Session):
        if not isinstance(session, Session):
            raise TypeError('Expected a Session object.')

        self._table('sessions')._insert(session)

    def _table(self, table_name: str):
        self._client.table(table_name)
        return self

    def _insert(self, data: BaseModel):
        self._client.insert(data)
        return self
