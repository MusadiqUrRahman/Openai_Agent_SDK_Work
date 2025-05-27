#  اس کوڈ میں ہم دکھائیں گے کہ ماڈل کو تمام ایجنٹس کو کیسے دیا جاتا ہے۔

# یا تھوڑا مزید خوبصورت انداز میں:

# 🚀 ماڈل کو ایک ساتھ کئی ایجنٹس کے ساتھ استعمال کرنے کا طریقہ

                     
#                    ===========================================
#                      🔹 Passing only one Model to All Agents
#                    ===========================================

# 📜 Note:
#         In this code, we demonstrate how a single model can be passed and shared
#         across multiple agents, making the setup efficient, clean, and easier to manage.
#         This run lavel. M.uzair say.



from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI


# Load environment variables
load_dotenv()

# OpenRouter client setup

my_client = AsyncOpenAI(
    api_key=os.getenv("OpenRouter_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Correct model from OpenRouter
my_model = OpenAIChatCompletionsModel(
    model="nvidia/llama-3.3-nemotron-super-49b-v1:free",  # ✅ Correct Model ID
    openai_client=my_client,
)
# Disable tracing
set_tracing_disabled(True)

# ✅Define the run configuration ?

# RunConfig is a simple set of instructions that tells a program how to run — like 
# which device to use, how much data to process at once, and how long to wait.


my_config = RunConfig(
    model=my_model,
    model_provider=my_client,

    
    #set_tracing_disabled=True,

    # max_tokens=1000,  # Maximum number of tokens to generate in the response
    # verbose=True,  # Whether to print detailed information during the run
    # temperature=0.7,  # Controls the randomness of the output (0.0 to 1.0)
    # top_p=1.0,  # Controls the diversity of the output (0.0 to 1.0)
    # frequency_penalty=0.0,  # Penalizes new tokens based on their existing frequency in the text so far
    # presence_penalty=0.0,  # Penalizes new tokens based on whether they appear in the text so far
    # stop=None,  # A string or list of strings that will cause the model to stop generating further tokens
    # # when encountered. If None, the model will not stop generating until max_tokens is reached.
    # # Example: stop=["\n", "END"] will stop generation when either "\n" or "END" is encountered.
    # # Note: The stop parameter is not supported by all models.
    # # Check the model documentation for details.
    )

# Define the agent
agent = Agent(
    name="Teacher",
    instructions="First answer in detailed English, then give a short beautiful Urdu explanation.",
    #model=my_model,
)

# Run the agent with a sample input
response = Runner.run_sync(
    starting_agent=agent,
    input="who is imran khan?",
    run_config=my_config,
    
)

# Print final output

print("\n📚 Final Response:\n")
print(response.final_output)



































































# #  اس کوڈ میں ہم دکھائیں گے کہ ماڈل کو تمام ایجنٹس کو کیسے دیا جاتا ہے۔

# # یا تھوڑا مزید خوبصورت انداز میں:

# # 🚀 ماڈل کو ایک ساتھ کئی ایجنٹس کے ساتھ استعمال کرنے کا طریقہ

                     
# #                    ===========================================
# #                      🔹 Passing only one Model to All Agents
# #                    ===========================================

# # 📜 Note:
# #         In this code, we demonstrate how a single model can be passed and shared
# #         across multiple agents, making the setup efficient, clean, and easier to manage.
# #         This run lavel. M.uzair say.



# from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, RunConfig
# from dotenv import load_dotenv
# import os
# from openai import AsyncOpenAI


# # Load environment variables
# load_dotenv()

# # OpenRouter client setup

# my_client = AsyncOpenAI(
#     api_key=os.getenv("OpenRouter_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
# )

# # Correct model from OpenRouter
# my_model = OpenAIChatCompletionsModel(
#     model="deepseek-chat",  # ✅ Correct Model ID
#     openai_client=my_client,
# )
# # Disable tracing
# set_tracing_disabled(True)

# # ✅Define the run configuration ?

# # RunConfig is a simple set of instructions that tells a program how to run — like 
# # which device to use, how much data to process at once, and how long to wait.


# my_config = RunConfig(
#     model=my_model,  # Model to use for the agent
#     model_provider=my_client

    
#     #set_tracing_disabled=True,

#     # max_tokens=1000,  # Maximum number of tokens to generate in the response
#     # verbose=True,  # Whether to print detailed information during the run
#     # temperature=0.7,  # Controls the randomness of the output (0.0 to 1.0)
#     # top_p=1.0,  # Controls the diversity of the output (0.0 to 1.0)
#     # frequency_penalty=0.0,  # Penalizes new tokens based on their existing frequency in the text so far
#     # presence_penalty=0.0,  # Penalizes new tokens based on whether they appear in the text so far
#     # stop=None,  # A string or list of strings that will cause the model to stop generating further tokens
#     # # when encountered. If None, the model will not stop generating until max_tokens is reached.
#     # # Example: stop=["\n", "END"] will stop generation when either "\n" or "END" is encountered.
#     # # Note: The stop parameter is not supported by all models.
#     # # Check the model documentation for details.
#     )

# # Define the agent
# agent = Agent(
#     name="Teacher",
#     instructions="First answer in detailed English, then give a short beautiful Urdu explanation.",
#     #model=my_model,
# )

# # Run the agent with a sample input
# response = Runner.run_sync(
#     starting_agent=agent,
#     input="who is imran khan?",
#     run_config=my_config,
    
# )

# # Print final output

# print("\n📚 Final Response:\n")
# print(response.final_output)
