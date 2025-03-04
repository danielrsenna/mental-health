import os

import dotenv
from supabase import create_client
from pymongo import MongoClient
from pydantic import BaseModel


dotenv.load_dotenv()

class _SupaBase:

    def __init__(self, url: str, key: str, table_name: str):
        self._client = create_client(url, key)
        self._table = self._client.table(table_name)

    def table(self, table_name: str):
        self._table = self._client.table(table_name)

    def insert(self, data: dict):
        self._table.insert(data).execute()


class _MongoDB:

    def __init__(self, url: str, table_name: str, database_name: str = 'mental_health'):
        self._client = MongoClient(url, uuidRepresentation="standard")
        self._collection = self._client[database_name][table_name]

    def table(self, table_name: str):
        self._collection = self._client[table_name]

    def insert(self, model: BaseModel):
        self._collection.insert_one(model.model_dump())


class DatabaseClient:

    MODELS = {
        'supabase': lambda: _SupaBase(url=os.environ['SUPABASE_URL'], key=os.environ['SUPABASE_KEY'], table_name='mental_health'),
        'mongodb': lambda: _MongoDB(url=os.environ['MONGO_URL'], table_name='mental_health')
    }

    def __init__(self, model: str):
        if model not in self.MODELS:
            raise ValueError(f'Model {model} not found.')

        self._client = self.MODELS[model]()

    def table(self, table_name: str):
        self._client.table(table_name)
        return self

    def insert(self, data: dict):
        return self._client.insert(data)
