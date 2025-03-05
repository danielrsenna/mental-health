import os
from typing import AsyncGenerator

import dotenv
from openai import AsyncOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ..prompts import main_prompt  


dotenv.load_dotenv()


class _BasicGptClient:

    model='gpt-4o-mini'

    def __init__(self, api_key: str=os.environ['OPENAI_API_KEY']):
        self._client = AsyncOpenAI(api_key=api_key)

    async def answer(self, prompt: str) -> AsyncGenerator[str, None]:
        session = await self._client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'user', 'content': prompt}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        _answer = ''
        async for item in session:
            if hasattr(item.choices[0].delta, 'content'):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                _answer += item.choices[0].delta.content

                yield _answer

class _LangchainGptClient:
    def __init__(self, api_key: str = os.environ['OPENAI_API_KEY']):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            openai_api_key=api_key
        )

        # Criando o template de prompt com base no arquivo prompts.py
        self.prompt_template = ChatPromptTemplate.from_template(main_prompt)

        # Criando a "chain" combinando o template com o modelo OpenAI
        self.main_chain = self.prompt_template | self.llm 

    async def answer(self, chat_history: list[tuple[str, str]], user_input: str) -> str:
        # Formatar o histórico da conversa
        messages_history = '\n'.join(
            f'Human: {q}\nAssistant: {a}'
            for q, a in chat_history
        )

        # Chamando o modelo OpenAI via LangChain
        response = await self.main_chain.ainvoke({
            "messages_history": messages_history,
            "input": user_input
        })

        return response.content
    
    
GptClient = _LangchainGptClient
