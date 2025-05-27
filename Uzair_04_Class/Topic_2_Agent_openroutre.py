from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os 
#import asyncio  

load_dotenv()
set_tracing_disabled(True)

# provider = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

provider = AsyncOpenAI(
    api_key=os.getenv("OpenRouter_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
   
)

# creating model
model = OpenAIChatCompletionsModel(
    model="nvidia/llama-3.3-nemotron-super-49b-v1:free",              #"gemini-2.0-flash-exp",
    openai_client=provider
)


# creating agent
async def create_agent(user_query):
    My_Agent1 = Agent(
        name="Assistant",
        instructions="You will response to user query",
        model=model
    )
    #return My_Agent
    response = await Runner.run(starting_agent=My_Agent1, input= user_query)

    #print(response.final_output)
    return response.final_output 
#asyncio.run(create_agent())