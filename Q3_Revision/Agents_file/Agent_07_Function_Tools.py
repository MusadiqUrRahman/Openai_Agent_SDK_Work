#                 ============================================================
#                 Tools and Functions for Agent using Chainlit and show history
#                 ============================================================



from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv, find_dotenv
import os
import chainlit as cl
from agents.tool import function_tool
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging() # that will enable verbose logging to stdout. show the background process of the agent / code.

load_dotenv(find_dotenv())

set_tracing_disabled(True)

@function_tool
#@cl.step(type="weather tool")
def get_weather(location: str, unit: str = "C") -> str:
  """
  Fetch the weather for a given location, returning a short description.
  """
  # Example logic
  return f"The weather in {location} is 22 degrees {unit}."

My_agent1 = Agent(
    name="Assistant",
    instructions="You will respond to user query",         
    model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",), 
    tools=[get_weather],  # Register the tool with the agent
    )

@cl.on_chat_start
async def start():
    # Initialize history in user session
    cl.user_session.set("history", [])
    
    # Send welcome message
    await cl.Message(
        content="Hello! I am your assistant. How can I help you today? 🤖",
    ).send()
#_______________________________________________________________________________

@cl.on_message
async def musadiq(message: cl.Message):
    # Retrieve chat history (fixing typo from "histroy" to "history")
    my_history = cl.user_session.get("history") or []

    # Add user message to history
    my_history.append({"role": "user", "content": message.content})

    # Run the agent with the conversation history as input
    result = await Runner.run(
        starting_agent=My_agent1,
        input=my_history,
    )

    # Add assistant's response to history
    my_history.append({"role": "assistant", "content": result.final_output})

    # Update session history
    cl.user_session.set("history", my_history)

    # Send agent's response
    await cl.Message(
        content=f"Agent Response 🤖 {result.final_output}",
    ).send()











    
    




