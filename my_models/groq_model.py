from my_config.groq_config import groq_client
from agents import OpenAIChatCompletionsModel
MODEL=OpenAIChatCompletionsModel(
    model="openai/gpt-oss-20b",
    openai_client=groq_client

)