#                   ===============================================================
#"""                  🔹 Simple Agent Powered by Gemini and sync🤖✨      """
#                   ===============================================================
# 📝 Short Note:
#               A lightweight agent built using the Gemini API for seamless AI integration. 🔑🚀




from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled      #AsyncOpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

set_tracing_disabled(True)


my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
)



My_Agent = Agent(
    name="Assistant",
    instructions="You will response to user query answer english and urdu",
    model=my_model,

)
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = Runner.run_sync(
       starting_agent=My_Agent,
       input=user_input,
    )

    print(response.final_output)
    #print(f"Assistant: {response}")
    #print(f"Welcome syed: {response.final_output}")



# # Example of running the agent

# # running agent
# response = Runner.run_sync(
#     starting_agent=My_Agent,
#     input="Hello, how are you?",
# )
# print(response.final_output)