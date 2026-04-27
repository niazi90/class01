from my_models.groq_model import MODEL
from agents import Agent
Groq_agent=Agent(
    name='student',
model=MODEL,
instructions="give me short answer "
)