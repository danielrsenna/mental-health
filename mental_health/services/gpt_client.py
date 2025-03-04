import os
from typing import AsyncGenerator

import dotenv
from openai import AsyncOpenAI


dotenv.load_dotenv()

class GptClient:

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
