from agents import Agent, Runner , OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
#==================================================================

#This is where I have setup the API.

load_dotenv()

my_provider  = AsyncOpenAI(
     api_key=os.getenv("GEMINI_API_KEY"),
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/", # I picked this up from Google Documention
)

my_model = OpenAIChatCompletionsModel(
     
     model = "gemini-2.0-flash-exp",
     openai_client = my_provider,
)



Agent1 = Agent(
    
    name = "Assitant",
     instructions = "A helpful assitant that can answer question and provide information",
     model = my_model
)

response = Runner.run_sync(
    starting_agent=Agent1,
    input="who is imran khan"
)

print(response.final_output)
#====================================================================

# def run():
#      agent = Agent(name="Assistant", 
#                    instructions="You are a helpful assistant",
#                    model=my_model,
#                    )

#      result = Runner.run_sync(agent, "tell me about pakistan.")
#      print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.

