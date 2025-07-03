#                   ===========================================================
#"""                         🔹 Simple Agent Powered by litellm and sync🤖✨                     """
#                   ===========================================================

from agents import Agent, Runner, set_tracing_disabled #OpenAIChatCompletionsModel
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os

load_dotenv()
set_tracing_disabled(True)

My_agent1 = Agent(
    name="Assistant",
    instructions="You will respond to user query",          # the first gemini is provider.. and second model name
    model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",) 

    )

response1 = Runner.run_sync(
    starting_agent=My_agent1,
    input="Hello, how are you?",
)

print(response1.final_output)