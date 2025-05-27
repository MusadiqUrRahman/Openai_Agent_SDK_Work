# ہم اب اس کوڈ میں کیا کریں گے ہم اب اس کوڈ میں ہر ایجنٹ کو الگ الگ ماڈل کے ساتھ ٹیسٹ کریں گے

#     ======================================================================================

#       🔹Testing Agents with Different Models — Separate Model Testing for Each Agent 🤖✨

#     ======================================================================================

# In this code, we will test each agent with a different model.   
# ✅Note: 
    #   Each agent in this setup uses a different AI model to perform tasks. Testing them separately helps us understand the strengths and differences of each model, making it easier to choose the best one for specific needs. 🚀

from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
from agents import set_default_openai_api, set_default_openai_client
from dotenv import load_dotenv  
import os
from openai import AsyncOpenAI


# Load environment variables
load_dotenv()

# OpenRouter client setup

my_client = AsyncOpenAI(
    api_key=os.getenv("OpenRouter_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Set default OpenAI API key and client

set_default_openai_api("chat_completions")
set_default_openai_client(my_client)

# Disable tracing
set_tracing_disabled(True)


# Define the agent
agent1 = Agent(
    name="Teacher",
    instructions="First answer in detailed, then give a short beautiful step by step explanation.",
    model= "microsoft/mai-ds-r1:free"
)

# Define the agent with a different model
agent2 = Agent(
    name="Teacher",
    instructions="First answer in detailed, then give a short beautiful step by step explanation.",
    model= "agentica-org/deepcoder-14b-preview:free"  
)

# Define the agent with another different model
agent3 = Agent(
    name="Teacher",
    instructions="First answer in detailed, then give a short beautiful step by step explanation.",
    model= "nvidia/llama-3.3-nemotron-super-49b-v1:free"  # very bast model long and good response
)



# Run the agent with a sample input

response1 = Runner.run_sync(
    starting_agent=agent1,
    input=input("Enter your question: ===> Q:"),  # Get user input for the question
)

response2 = Runner.run_sync(
    starting_agent=agent2,
    input= input("Enter your question: ===> Q:"),  
)

response3 = Runner.run_sync(
    starting_agent=agent3,
    input= input("Enter your question: ===> Q:"),
)


# Print final output for each agent

print("\n📚 Final Response from Agent 1:\n")
print(response1.final_output)


print("\n📚 Final Response from Agent 2:\n")
print(response2.final_output)


print("\n📚 Final Response from Agent 3:\n")
print(response3.final_output)
