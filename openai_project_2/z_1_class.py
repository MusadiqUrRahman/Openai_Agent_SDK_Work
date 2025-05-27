# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# from dotenv import load_dotenv

# import os

# load_dotenv()

# my_model = OpenAIChatCompletionsModel(
#     model = "gemini-2.0-flash-exp",           
#     openai_client=AsyncOpenAI()
#     api_key = os.getenv("GEMINI_API_KEY"),
     
#     # Replace with the actual base URL for the Gemini model
#      bas_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
    
# )

# agent = Agent(
#     name = "Agent",
#     instructions= "Answer the question and perform the task.",
#     model= my_model,
# )
    
# response = Runner.run_sync(
# starting_agent = agent,
# input = "who is imram khan?",

# )
# print(response)



# # agent = Agent(
# #     name="Gemini",
# #     description="A Gemini agent that can answer questions and perform tasks.",
# #     api_key=os.getenv("OpenRouter_API_KEY"),
# #     model="google/gemini-2.5-pro-exp-03-25:free",
# #     temperature=0.7,
# #     max_tokens=1000,
# # )
# ##===============================================================================


from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI  # Ensure this is the correct module for AsyncOpenAI
#from chainlit import cl  # Ensure you have the correct import for your chat library

import chainlit as cl



# Load environment variables from .env file
load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OpenRouter_API_KEY"),
    base_url="https://openrouter.ai/api/v1",  
    # Ensure this is the correct base URL for the OpenRouter API
    # You can also set other parameters like organization, timeout, etc. if needed
    # Replace with the actual base URL for the OpenRouter API
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

@cl.on_message
async def main(message: cl.Message):
   
    content = Runner.run_sync(agent,message.content)
    await cl.Message(
        content=content.final_output,
    ).send() 

# # Print final output
# print("\n📚 Final Response:\n")
# print(response.final_output)


































































# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# import os
# from openai import AsyncOpenAI
# from chainlit import on_message
# from chainlit.message import Message
# import chainlit as cl

# # Load environment variables
# load_dotenv()

# # OpenRouter Client Setup
# client = AsyncOpenAI(
#     api_key=os.getenv("OpenRouter_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )

# # LLM Model Setup
# my_model = OpenAIChatCompletionsModel(
#     model="openai/gpt-3.5-turbo",
#     openai_client=client,
# )

# # Disable tracing
# set_tracing_disabled(True)

# # Main Agent
# agent = Agent(
#     name="Teacher",
#     instructions=(
#         "Answer the question and perform the task. "
#         "First answer in detailed English, then give a short beautiful Urdu explanation."
#     ),
#     model=my_model,
# )

# # ✅ Chat History store (per user session)
# chat_history = []

# # Main message handler
# @on_message
# async def main(message: cl.Message):
#     user_input = message.content

#     # Store user message
#     chat_history.append(f"User: {user_input}")

#     # Process the message with the agent
#     content = Runner.run_sync(agent, user_input)

#     # Store agent's response
#     chat_history.append(f"Bot: {content.final_output}")

#     # Combine and show chat history
#     history_output = "\n".join(chat_history[-10:])  # last 10 messages
#     await Message(content=history_output).send() # type: ignore

































































# Run the agent with a sample input




# # Example of using OpenRouter API with Python
# # This example assumes you have the OpenRouter API key stored in a .env file
# # and the required libraries installed.



# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# import os
# from openai import AsyncOpenAI

# # Load environment variables
# load_dotenv()

# # OpenRouter client setup
# api_key = os.getenv("OpenRouter_API_KEY")
# if not api_key:
#     raise Exception("API Key not found! Please check your .env file.")

# client = AsyncOpenAI(
#     api_key=api_key,
#     base_url="https://openrouter.ai/api/v1",
# )

# # Correct model from OpenRouter
# my_model = OpenAIChatCompletionsModel(
#     model="deepseek-chat",  # ✅ Correct Model ID
#     openai_client=client,
# )

# # Disable tracing
# set_tracing_disabled(True)

# # Define the agent
# agent = Agent(
#     name="Teacher",
#     instructions="First answer in detailed English, then give a short beautiful Urdu explanation.",
#     model=my_model,
# )

# # Run the agent
# response = Runner.run_sync(
#     starting_agent=agent,
#     input="Who is Imran Khan?",
# )

# print("\n📚 Final Output:\n")
# print(response.final_output)


