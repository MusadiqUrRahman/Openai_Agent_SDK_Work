
#                  ===============================================================
"""                        Simple Agent Powered by Gemini & Asyncio, run_streame 🤖⚡ """ 
#                  ===============================================================
# 📝 Short Note:
#              A lightweight AI agent built using the Gemini API and
#              Python's asyncio module for efficient asynchronous operations. 🔑🌀


from agents import Agent , Runner ,OpenAIChatCompletionsModel, set_tracing_disabled #AsyncOpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio 
from openai.types.responses import ResponseTextDeltaEvent


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
# MyAgent = Agent(
#     name = "Assistant",
#     instructions= "You will response to user query",
#     model = model
# )

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
        model=model
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(main())




