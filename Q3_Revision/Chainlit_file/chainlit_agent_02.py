#               ===========================================================
#                   Smart Agent with Function Tool(tavily) Integration 🛠️🤖✨
#               ===========================================================


from agents import Agent, function_tool #Runner #,set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

@function_tool
def weather_tool(user_input:str):
    """search tools"""
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    response = tavily_client.search(query=user_input)

    #print(response)
    return response
    #return json.dumps(response)


def agent_creator() -> Agent:
    Myagent = Agent(
        name = "Assistant",
        instructions = "You are a helpful assistant.",
        model = LitellmModel(
            api_key=os.getenv("GEMINI_API_KEY"), 
            model="gemini/gemini-2.0-flash-exp",),
            tools=[weather_tool],
        )
    return Myagent


    