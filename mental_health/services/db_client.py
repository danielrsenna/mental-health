from supabase import create_client
from pymongo import MongoClient
from pydantic import BaseModel

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
        'supabase': lambda url, key, table_name : _SupaBase(url, key, table_name),
        'mongodb': lambda url, _, table_name : _MongoDB(url, table_name)
    }

    def __init__(self, url: str, key: str, table_name: str, model: str):
        if model not in self.MODELS:
            raise ValueError(f'Model {model} not found.')

        self._client = self.MODELS[model](url, key, table_name)

    def table(self, table_name: str):
        self._client.table(table_name)
        return self

    def insert(self, data: dict):
        return self._client.insert(data)
