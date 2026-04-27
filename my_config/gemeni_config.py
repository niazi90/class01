from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from decouple import config
gemeni_base_url=config('GEMENI_BASE_URL')
gemeni_key=config('GEMENI_API_KEY')
gemeni_client=AsyncOpenAI(
    base_url=gemeni_base_url,
    api_key=gemeni_key
)