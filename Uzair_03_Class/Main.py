#                   ================================================================
"""                    Simple Agent with Gemini and litellm, Asyncio & Chainlit 🤖🔗✨          """
#                   ================================================================
# 📝 Short Note:
#              A lightweight AI agent built using the Gemini API and
#              Python's asyncio, powered by Chainlit to create and run multiple agents,
#              including integrations with OpenAI. 🔑🌀💡🤝



#               =====================
#"""                 📌  Step 1️                             """
#               =====================


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

# @cl.on_message
# async def main(message: cl.Message):

#     response = Runner.run_sync(
#         starting_agent=agent,
#         input=message.content,  # Get user input for the question
#     )

#     await cl.Message(
#         content= f"AI Agent 🤖: {response.final_output}",).send()
 
#______________________________________________________________________
# # @cl.on_message
# # async def main(message: cl.Message):
   
# #     response = Runner.run_sync(starting_agent=agent, input=message.content)
# #     await cl.Message(content=response.final_output,).send() 

# # # Print final output
# # # print("\n📚 Final Response:\n")
# # # print(main.final_output)
#=====================================================================================================


#               =====================
#"""                 📌  Step 2️                            """
#               =====================

# from litellm import completion
# import os
# from dotenv import load_dotenv

# # Load API Key                     #$env:PYTHONUTF8=1 >> python main.py

# load_dotenv()

# SYED_API_KEY =  os.getenv("GEMINI_API_KEY")

# messages = [{"role": "user", "content": "Hello, how are you?"}]

# response = completion(model="gemini/gemini-2.0-flash-exp", messages=messages)

# print(response['choices'][0]['message']['content'])

# print(response)

#__________________________________________________________________________

# Call Gemini model via LiteLLM
# response = completion(
#     model="gemini/gemini-pro",
#     messages=[{"role": "user", "content": "Hello Gemini, what can you do?"}]
# )

# Print response
#print("Gemini:", response['choices'][0]['message']['content'])
#print(response)

###___________________________________________________________________________


# #Call OpenRouter model via LiteLLM
# def syed(user_input):
#     result = completion(
#         model="openrouter/gemini-2.0-flash-exp",
#         messages=[{"role": "user", "content": user_input}]
#     )
#     return (result['choices'][0]['message']['content'])


#=====================================================================================================

#               =====================
#"""                 📌  Step 3️⃣                             """
#               =====================

# #============== In this we are converting from one file to the other file ================

# # LiteLLM سے completion function امپورٹ کر رہے ہیں
# from litellm import completion

# # سسٹم سے environment variables حاصل کرنے کے لیے os ماڈیول
# import os

# # .env فائل سے API keys وغیرہ لوڈ کرنے کے لیے
# from dotenv import load_dotenv

# # .env فائل لوڈ کریں تاکہ ہم اپنی API key استعمال کر سکیں
# load_dotenv()

# # اپنی Gemini API Key .env فائل سے حاصل کریں
# SYED_API_KEY = os.getenv("GEMINI_API_KEY")

# def syed(user_input):
#     # LiteLLM کے completion function کو کال کریں
#     answer = completion(
#         model="gemini/gemini-2.0-flash-exp",  # ماڈل کا نام
#         messages=[{"role": "user", "content": user_input}] , # یوزر کا پیغام
#         stream=False                    # یہاں stream=False ہے تاکہ مکمل جواب ایک بار میں مل سکے
#     )
#     return (answer['choices'][0]['message']['content'])  # type: ignore # AI کا جواب واپس کریں

# # response = syed("Hello, how are you?")
# # print(response)

#_____________________________________________________________________________________
    
# # یوزر کا پیغام (پرومپٹ) جو ہم AI کو بھیجنا چاہتے ہیں
# messages = [{"role": "user", "content": "Hello, how are you?"}]

# # LiteLLM کو کال کر رہے ہیں — یہاں stream=False تاکہ ہمیں مکمل ریسپانس ملے
# response = completion(
#     model="gemini/gemini-2.0-flash-exp",  # ماڈل نیم
#     messages=messages,
#     stream=False  # streaming بند ہے تاکہ ہم dictionary جیسا رسپانس لے سکیں
# )

# # AI کا جواب پرنٹ کریں
# print(response['choices'][0]['message']['content'])

# # پورا رسپانس (debug یا مکمل معلومات کے لیے)
# #print(response)

#=====================================================================================================

# #               =====================
# """                 📌  Step 4️⃣                             """
# #               =====================


# from agents import Agent , Runner ,OpenAIChatCompletionsModel, set_tracing_disabled #AsyncOpenAI
# from openai import AsyncOpenAI
# from dotenv import load_dotenv
# import os
# import asyncio

# load_dotenv()

# set_tracing_disabled(True)

# provider = AsyncOpenAI(
#         api_key = os.getenv("GEMINI_API_KEY"),
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )

# # creating model
# model = OpenAIChatCompletionsModel(
#     model = "gemini-2.0-flash-exp",
#     openai_client = provider

# ) 

# # creating agent
# MyAgent = Agent(
#     name = "Assistant",
#     instructions= "You will response to user query",
#     model = model
# )

# #running agent
# async def main():
#     response  = await Runner.run(starting_agent = MyAgent, input = "Hello, how are you?",)
#     print(response.final_output)


# asyncio.run(main())

# # response  = Runner.run_sync(
# #     starting_agent = MyAgent,
# #     input = "Hello, how are you?",
# # )

# # print(response.final_output)
















































# from litellm import completion
# import os
# from dotenv import load_dotenv


# # Load environment variables from .env file
# load_dotenv()

# response = completion(
#   model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
#   messages=[{ "content": "Hello, how are you?","role": "user"}]
# )
# #print(response["choices"][0]["message"]["content"])
# print(response)

































