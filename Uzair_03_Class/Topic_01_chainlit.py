#                   ================================================================
"""                    Simple Agent with Gemini and litellm, Asyncio & Chainlit 🤖🔗✨                     """
#                   ================================================================

#import chainlit as cl


# #               =====================
# """                 📌  Step 1️⃣                             """
# #               =====================


# # @cl.on_message
# # async def main1(message: cl.Message):
# #     # Your custom logic goes here...

# #     # Send a response back to the user
# #     await cl.Message(
# #         content=f"Received: {message.content}",
# #     ).send()



# #               =====================
# """                 📌  Step 3️⃣                             """
# #               =====================

# # @cl.on_message
# # async def main2(message: cl.Message):
# #     # Your custom logic goes here...

# #     user_input = message.content

# #     #added_message = f"User said: {user_input}"

  
# #     # Send a response back to the user
# #     await cl.Message(content=user_input).send()


# #               =====================
# """                 📌  Step 4️⃣                             """
# #               =====================

# # @cl.on_message
# # async def main3(message: cl.Message):
# #     # Your custom logic goes here...

# #     user_input = message.content

# #     added = int(user_input) + 10

# #     #final_message = f"User said: {user_input}, added 10: {added}"

# #     # Send a response back to the user
# #     await cl.Message(content=added).send() # type: ignore



# #               =====================
#"""                 📌  Step 5️⃣                             """
# #               =====================

#============== In this we are converting from one file to the other file ================

import chainlit as cl

#from Topic_00_Agent import syed

from Topic_00_Agent import musadiq
import asyncio

@cl.on_chat_start

async def main1():
    # This function will be called when the chat starts
    await cl.Message(content="👋 Welcome to the chat!").send()  

        # This message will be sent to the user when the chat starts

@cl.on_message
async def main2(message: cl.Message):
    # Your custom logic goes here...

    user_input = message.content

    #result = syed(user_input)
    result = asyncio.run(musadiq(user_input))

   # added_message = f"User said: {user_input}"

  
    # Send a response back to the user
    await cl.Message(content=result).send()
#________________________________________________________________
# # @cl.on_stop
# # async def main3():
# #     # This function will be called when the chat stops
# #     await cl.Message(content="👋 Goodbye!").send()

# #     # This message will be sent to the user when the chat stops

# # @cl.on_chat_end
# # async def main4():
# #     # This function will be called when the chat ends
# #     await cl.Message(content="👋 Chat has ended!").send()

# #     # This message will be sent to the user when the chat ends



# #               =====================
#"""                 📌  Step 6️                             """
# #               =====================


# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# import os
# from openai import AsyncOpenAI  # Ensure this is the correct module for AsyncOpenAI
# #from chainlit import cl  # Ensure you have the correct import for your chat library

# import chainlit as cl



# # Load environment variables from .env file
# load_dotenv()

# client = AsyncOpenAI(
#     api_key=os.getenv("OpenRouter_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",  
#     # Ensure this is the correct base URL for the OpenRouter API
#     # You can also set other parameters like organization, timeout, etc. if needed
#     # Replace with the actual base URL for the OpenRouter API
# )

# my_model = OpenAIChatCompletionsModel(
#     model="openai/gpt-3.5-turbo",
#     openai_client=client,
# )


# # Disable tracing for the agent
# set_tracing_disabled(True)  # Uncomment this line if you want to disable tracing


# # Define the agent
# agent = Agent(
#     name="Teacher",
#     instructions="Answer the question and perform the task and" \
#                   "First answer in detailed English, then give a short beautiful Urdu explanation..",
#     model=my_model,
# )

# # response = Runner.run_sync(
# #     starting_agent=agent,
# #     input=input("Enter your question: ===> Q:"),  # Get user input for the question
# # #)
# @cl.on_chat_start

# async def main1():
#     # This function will be called when the chat starts
#     await cl.Message(content="👋 Welcome to the chat!").send()  


# @cl.on_message
# async def main(message: cl.Message):

#     response = Runner.run_sync(
#         starting_agent=agent,
#         input=message.content,  # Get user input for the question
#     )

#     await cl.Message(
#         content= f"AI Agent 🤖: {response.final_output}",).send()






















# # @cl.on_message
# # @greet_user("👋 السلام علیکم! خوش آمدید")  # ہم یہاں argument دے رہے ہیں
# # async def main(message: cl.Message):
# #     await cl.Message(content=f"آپ نے فرمایا: {message.content}").send()




