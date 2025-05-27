#                      =========================================================
#                         Streaming Agent with History on Chainlit 🔗🌊🧠
#                      =========================================================


from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI 
import chainlit as cl
from openai.types.responses import ResponseTextDeltaEvent



# Load environment variables from .env file
load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OpenRouter_API_KEY"),
    base_url="https://openrouter.ai/api/v1",  
)

my_model = OpenAIChatCompletionsModel(
    model="openai/gpt-3.5-turbo",
    openai_client=client,
)


# Disable tracing for the agent
set_tracing_disabled(True)  # Uncomment this line if you want to disable tracing


# Define the agent
agent = Agent(
    name="Teacher",
    instructions="Answer the question and perform the task and" \
                  "First answer in detailed English, then give a short beautiful Urdu explanation..",
    model=my_model,
)

# response = Runner.run_sync(
#     starting_agent=agent,
#     input=input("Enter your question: ===> Q:"),  # Get user input for the question
# #)
@cl.on_chat_start

async def main1():
    # This function will be called when the chat starts
    await cl.Message(content="👋 Welcome to the chat!").send() 

    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])
    # You can also send a welcome message or perform any other initialization here
    await cl.Message(content="✨ Hi! I am Syed, your AI assistant. How can I help you today?✨").send()
    
@cl.on_message
async def main(message: cl.Message):
    # This function will be called when a message is received
    # You can process the message and send a response here

    # Retrieve the chat history from the session.
    my_history = cl.user_session.get("chat_history") or []

    my_message = cl.Message(content="Thinking...")
    await my_message.send()

    # Append the new message to the chat history.
    my_history.append({"role": "user", "content": message.content})
    
    response = Runner.run_streamed(starting_agent=agent, input=my_history)

    # streaming
    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            my_message.content += event.data.delta
            await my_message.update()
            print(event.data.delta, end="", flush=True)

    # Append the assistant's response to the chat history.
    my_history.append({"role": "assistant", "content": my_message.content})

    # Update the chat history in the session.
    cl.user_session.set("chat_history", my_history)

    # Send the final output to the user
    #await cl.Message(content=f"✨Syed Say This✨: {my_message.content}",).send()

# #================================================================================



# from agents import Agent , Runner, set_tracing_disabled
# from agents.extensions.models.litellm_model import LitellmModel
# from openai.types.responses import ResponseTextDeltaEvent
# from dotenv import load_dotenv
# import os
# import asyncio
# import chainlit as cl


# load_dotenv()

# set_tracing_disabled(True)
# # creating agent

# ouragent = Agent(
#     name="Assistant",
#     instructions="You will respond to user query",         
#     model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",) 
# )

# @cl.on_chat_start
# async def start():
#     await cl.Message(
#         content="✨ Hi! I am Syed, your AI assistant. How can I help you today?✨").send()
    
#     # Initialize an empty chat history in the session.
#     cl.user_session.set("chat_history", [])

# @cl.on_message
# async def main1(message: cl.Message):
    
#     # Retrieve the chat history from the session.
#     my_history = cl.user_session.get("chat_history") or []

#     # Append the new message to the chat history.
#     my_history.append({"role": "user", "content": message.content})
    

#     response = Runner.run_streamed(starting_agent=ouragent, input=my_history)

#     # result =  Runner.run_streamed(starting_agent=ouragent1, input=user_input,)

#     async for event in response.stream_events():
#         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             print(event.data.delta, end="", flush=True)
         
        
#         # print(response.final_output)

# asyncio.run(main1())
    
# # asyncio.run(main())


# # #==================================================================================================


