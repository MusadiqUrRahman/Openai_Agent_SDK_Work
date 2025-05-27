# 
# 
#                         ===========================================================
#                               Streaming Agent Powered by LiteLLM 🌊🤖⚡
#                         ===========================================================


from agents import Agent , Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from openai.types.responses import ResponseTextDeltaEvent
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

    while True:    
        user_input = input("User: ")
        if user_input.lower() == "stop":
            break
        result =  Runner.run_streamed(starting_agent=My_agent1, input=user_input,)

        async for event in result.stream_events():
         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
         
        
        # print(response.final_output)

asyncio.run(main())        

# #==================================================================================================


# from agents import Agent, Runner, ItemHelpers, set_tracing_disabled
# from agents.extensions.models.litellm_model import LitellmModel
# from dotenv import load_dotenv
# import os
# import asyncio

# load_dotenv()
# set_tracing_disabled(True)

# async def main():
#     My_agent1 = Agent(
#         name="Assistant",
#         instructions="You will respond to user query",
#         model=LitellmModel(
#             api_key=os.getenv("GEMINI_API_KEY"),
#             model="gemini/gemini-2.0-flash-exp",
#         )
#     )

#     while True:
#         user_input = input("User: ")
#         if user_input.lower() == "stop":
#             break

#         result = Runner.run_streamed(starting_agent=My_agent1, input=user_input)

#         async for event in result.stream_events():
#             # Print event for debugging
#             print("Event:", event)

#             # Safe access pattern
#             item = getattr(event, "output", None) or getattr(event, "data", None) or None

#             if item:
#                 item_type = getattr(item, "type", None)
#                 if item_type == "tool_call_output_item":
#                     print(f"Tool output: {getattr(item, 'output', '')}")
#                 elif item_type == "message_output_item":
#                     print(ItemHelpers.text_message_output(item))
#             else:
#                 print("⚠ Unknown event structure or no item found.")

# asyncio.run(main())

        

