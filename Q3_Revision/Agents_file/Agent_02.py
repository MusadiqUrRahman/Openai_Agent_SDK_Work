#                    ===========================================
#                      🔹 Passing only one Model to All Agents
#                    ===========================================

from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv  
import os

# Load environment variables
load_dotenv()

# OpenRouter client setup
my_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Pass the client to the model only
my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=my_client,
)

# Agents
My_agent1 = Agent(
    name="Assistant",
    instructions="You will respond to user query",
)

My_agent2 = Agent(
    name="Assistant",
    instructions="You will respond to user query",
)

# ❌ ERROR here was passing my_client to model_provider
# ✅ FIX: just pass the model, NOT the client directly
my_config = RunConfig(
    model=my_model,
    tracing_disabled=True,
)

# Agent running
response1 = Runner.run_sync(
    starting_agent=My_agent1,
    input="Hello, how are you?",
    run_config=my_config
)

response2 = Runner.run_sync(
    starting_agent=My_agent2,
    input="Hello, how are you?",
    run_config=my_config
)

print(response1.final_output)
print(response2.final_output)




















# from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled      #AsyncOpenAI
# from openai import AsyncOpenAI
# from dotenv import load_dotenv  
# import os
# #from agents import set_default_openai_api, set_default_openai_client

# # # Load environment variables
# load_dotenv()

# # # OpenRouter client setup

# my_client = AsyncOpenAI(
#     api_key=os.getenv("OpenRouter_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
# )

# my_model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash-exp",
#     openai_client=my_client,
# )

# My_agent1 = Agent(
#     name="Assistant",
#     instructions="You will response to user query",
# )

# My_agent2 = Agent(
#     name="Assistant",
#     instructions="You will response to user query",
# )

# my_config = RunConfig(
#     model = my_model,
#     model_provider = my_client,
#     tracing_disabled=True,

# )

# #agent running
# response1 = Runner.run_sync(
#     starting_agent=My_agent1,
#     input="Hello, how are you?",
#     run_config=my_config
# )

# response2 = Runner.run_sync(
#     starting_agent=My_agent2,
#     input="Hello, how are you?",
#     run_config=my_config
# )
# print(response1.final_output)
# print(response2.final_output)


