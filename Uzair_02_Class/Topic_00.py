# This is a simple agent that uses the OpenAI API to generate text completions.
# It takes a prompt as input and returns the generated text as output.
# It uses the OpenAIChatCompletionsModel class to create a model object that can be used to generate text completions.
# It uses the Agent class to create an agent object that can be used to generate text completions.
# It uses the Runner class to run the agent and get the generated text as output.
# It uses the set_tracing_disabled function to disable tracing for the agent.
# It uses the load_dotenv function to load environment variables from a .env file.
# It uses the AsyncOpenAI class to create an OpenAI client that can be used to generate text completions.


#                   ===========================================================
"""                         🔹 Simple Agent Powered by Gemini and sync🤖✨                     """
#                   ===========================================================
# 📝 Short Note:
#               A lightweight agent built using the Gemini API for seamless AI integration. 🔑🚀




from agents import Agent , Runner ,OpenAIChatCompletionsModel, set_tracing_disabled #AsyncOpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
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
response  = Runner.run_sync(         
    starting_agent = MyAgent,
    input = "Hello, how are you?",
)

print(response)

# if you used only Runner.run() without await, it will not work.
# THAT ERROR COME: sys:1: RuntimeWarning: coroutine 'Runner.run' was never awaited


# because it is an async function and you need to use await to run it in an async context.
# if you want to run it in a sync context, you can use Runner.run_sync() instead.

# or you can use asyncio.run() to run it in an async context.
