from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from decouple import config
gemeni_base_url=config('BASE_URL')
gemeni_key=config('API_KEY')
gemeni_client=AsyncOpenAI(
    base_url=gemeni_base_url,
    api_key=gemeni_key
)