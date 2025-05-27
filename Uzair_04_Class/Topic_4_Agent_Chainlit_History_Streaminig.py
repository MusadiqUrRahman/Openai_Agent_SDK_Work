from agents import Agent , Runner #function_tool #,set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

#=================================✨ Agent ✨===================================

Myagent = Agent(
    name = "Assistant", 
    instructions = "You are a helpful assistant.",
    model = LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",))

#return Myagent

async def musadiq(user_query):
    response  = await Runner.run(starting_agent = Myagent, input = user_query,)

    return response.final_output
    #print(response.final_output)

#asyncio.run(musadiq("Hello, how are you?"))
asyncio.run(musadiq(input("Enter your question: ===> Q:")))


#===================================✨ Chainlit ✨=================================



