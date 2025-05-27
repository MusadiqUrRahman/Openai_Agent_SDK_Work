
#                  ===============================================================
"""                        Simple Agent Powered by Gemini & Asyncio 🤖⚡ """ 
#                  ===============================================================
# 📝 Short Note:
#              A lightweight AI agent built using the Gemini API and
#              Python's asyncio module for efficient asynchronous operations. 🔑🌀


from agents import Agent , Runner ,OpenAIChatCompletionsModel, set_tracing_disabled #AsyncOpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

set_tracing_disabled(True)

provider = AsyncOpenAI(
        api_key = os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# creating model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client = provider

)

# creating agent
MyAgent = Agent(
    name = "Assistant",
    instructions= "You will response to user query",
    model = model
)

# running agent
async def run_agent():
    response  = await Runner.run(
        starting_agent = MyAgent,
        input = "Hello, how are you?",
    )
    print(response.final_output)

asyncio.run(run_agent())

# if you used only Runner.run() without await, it will not work.
# THAT ERROR COME: sys:1: RuntimeWarning: coroutine 'Runner.run' was never awaited

# response  = Runner.run_sync(
#     starting_agent = MyAgent,
#     input = "Hello, how are you?",
# )

# print(response.final_output)





# # running agent
# response  = Runner.run_sync(
#     starting_agent = MyAgent,
#     input = "Hello, how are you?",
# )

# print(response.final_output)




