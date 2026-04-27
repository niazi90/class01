
from agents import Runner,set_tracing_disabled
from my_agents.gemeni_agent import agent
from my_agents.groq_agent import Groq_agent
from decouple import config
set_tracing_disabled(True)
print("Gemeni agents")
question=input("what question do you have ...")
res=Runner.run_sync(starting_agent=agent,input=question)
print(res.final_output)
print("Groq agents")
question=input("what question do you have...")
res=Runner.run_sync(starting_agent=Groq_agent,input=question)
print(res.final_output)