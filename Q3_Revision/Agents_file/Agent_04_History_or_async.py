# #                   ==================================================================
# #"""             🔹 Simple Agent Powered by litellm and ✨History/momery orasync function🤖 """
# #                   ==================================================================

# from agents import Agent , Runner ,set_tracing_disabled
# from agents.extensions.models.litellm_model import LitellmModel
# from dotenv import load_dotenv
# import os
# import asyncio

# load_dotenv()

# set_tracing_disabled(True)
# # creating agent

# MyAgent = Agent(
#     name = "Assistant",
#     instructions= "You will response to user query",
#     model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",) 
# )

# # running agent
# async def main():
#     response  = await Runner.run(starting_agent = MyAgent, input = "Hello, how are you?",)
#     print(response.final_output)

# asyncio.run(main())

# # response  = Runner.run_sync(
# #     starting_agent = MyAgent,
# #     input = "Hello, how are you?",

#==================================================================================================

from agents import Agent , Runner ,set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

set_tracing_disabled(True)
# creating agent

async def main ():

    My_agent1 = Agent(
        name="Assistant",
        instructions="You will respond to user query",         
        model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",) 
    )
    history = []
    while True:    
        user_input = input("User: ")
        history.append({"role": "user", "content": user_input})

        print("✨================✨ History ✨================✨")
        print(history)
        print("✨================✨ History ✨================✨")

        if user_input.lower() == "stop":
            break
        response = await Runner.run(starting_agent=My_agent1, input=history,)

        history.append({"role": "assistant", "content": response.final_output})
        print(response.final_output)

asyncio.run(main())        
        


    
   





