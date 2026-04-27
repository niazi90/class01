from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from decouple import config
groq_base_url=config('GROQ_BASE_URL')
groq_key=config('GROQ_API_KEY')
groq_client=AsyncOpenAI(
    base_url=groq_base_url,
    api_key=groq_key
)