from agents import Agent , Runner #function_tool #,set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv


load_dotenv()

async def agent_creator(user_query): #-> Agent:
    Myagent = Agent(
        name = "Assistant", 
        instructions = "You are a helpful assistant.",
        model = LitellmModel(api_key=os.getenv("GEMINI_API_KEY"),  
                             model="gemini/gemini-2.0-flash-exp",),)
    #return Myagent
    response = await Runner.run(starting_agent=Myagent, input= user_query)

    #print(response.final_output)
    return response.final_output 
#asyncio.run(agent_creator())


    