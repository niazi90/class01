from decouple import config
from agents import AsyncOpenAI,Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
base_url=config('BASE_URL')
key=config('API_KEY')
set_tracing_disabled(True)
question=input("what question do you have...")
instructions=input("Enter you instruction...")
gemini_client=AsyncOpenAI(
    base_url=base_url,
    api_key=key
)
Model=OpenAIChatCompletionsModel(
    model="gemini-3-flash-preview",
    openai_client=gemini_client

)
agent=Agent(name='teacher',model=Model,instructions=instructions)
res=Runner.run_sync(starting_agent=agent,input=question)
print(res.final_output)