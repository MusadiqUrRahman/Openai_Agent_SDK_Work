
# #               =====================
# """                 📌  Step 1️⃣                             """
# #               =====================

from agents import Agent , Runner ,OpenAIChatCompletionsModel, set_tracing_disabled #AsyncOpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
#import asyncio

load_dotenv()

set_tracing_disabled(True)

provider = AsyncOpenAI(
        api_key = os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# creating model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash-exp",
    openai_client = provider

) 

# creating agent
MyAgent = Agent(
    name = "Assistant",
    instructions= "You will response to user query",
    model = model
)

#running agent
##Asynchronous Code? 

async def musadiq(user_query):
    response  = await Runner.run(starting_agent = MyAgent, input = user_query,)
    return response.final_output
    #print(response.final_output)

#asyncio.run(musadiq("Hello, how are you?"))
#asyncio.run(musadiq(input("Enter your question: ===> Q:")))

#_______________________________________________________-
## Synchronous Code?

# def rahman(user_query):
#     response  = Runner.run_sync(
#         starting_agent = MyAgent,
#         input = user_query,
#     )
#     print(response.final_output)

# print(rahman("Hello, how are you?"))


#====================================================================================================

# #               =====================
# """                 📌  Step 3️⃣                             """
# #               =====================

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
