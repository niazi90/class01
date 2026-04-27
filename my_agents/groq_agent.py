from my_models.groq_model import MODEL
from agents import Agent
agent=Agent(
    name='teacher',
model=MODEL,
instructions="give me short answer "
)