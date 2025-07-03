# ============================================================
#         🤖 AI Assistant Agent with 15 Smart Tools using Chainlit
#         🔧 User Input Handling, Tool Execution, and History Tracking
# ============================================================

from agents import Agent, Runner, set_tracing_disabled
from agents.models.litellm_model import LitellmModel  # Adjusted import path; change as needed based on your project structure
from dotenv import load_dotenv, find_dotenv
import os
import chainlit as cl
from agents.tool import function_tool
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()  # Enable verbose logging to stdout
load_dotenv(find_dotenv())
set_tracing_disabled(True)

# -------------------- 15 Function Tools ----------------------

@function_tool
def calculate_price(price: float, discount: float) -> str:
    discounted = round(price - (price * discount / 100), 2)
    return f"💸 Price after {discount}% discount is {discounted} units."

@function_tool
def web_search(query: str) -> str:
    return f"🔍 You searched for: '{query}'. Please use Google for results."

@function_tool
def write_note(note: str) -> str:
    return f"📝 Note saved: '{note}'"

@function_tool
def start_timer(seconds: int) -> str:
    return f"⏳ Timer started for {seconds} seconds."

@function_tool
def add_numbers(a: int, b: int) -> int:
    return a + b

@function_tool
def give_idea() -> str:
    return "💡 Idea: Create an AI-powered language tutor!"

@function_tool
def meditate(minutes: int) -> str:
    return f"🧘‍♂️ Suggested meditation: {minutes} minutes."

@function_tool
def check_calendar(date: str) -> str:
    return f"📅 Selected date is {date}."

@function_tool
def listen_music(song: str) -> str:
    return f"🎶 Try listening to: '{song}'"

@function_tool
def greet_user(name: str) -> str:
    return f"👋 Hello {name}, how can I assist you today?"

@function_tool
def convert_temperature(celsius: float) -> str:
    fahrenheit = (celsius * 9/5) + 32
    return f"🌡️ {celsius}°C is {fahrenheit}°F."

@function_tool
def get_motivation() -> str:
    return "🚀 Don't stop until you're proud!"

@function_tool
def multiplication_table(number: int) -> str:
    return "📊 " + ", ".join([f"{number}x{i}={number*i}" for i in range(1, 11)])

@function_tool
def square_number(n: int) -> int:
    return n * n

@function_tool
def city_distance(from_city: str, to_city: str) -> str:
    # Sample logic; replace with real API or data for actual distances
    sample_distances = {
        ("lahore", "karachi"): 1215,
        ("lahore", "islamabad"): 375,
        ("karachi", "quetta"): 690
    }
    key = (from_city.lower(), to_city.lower())
    distance = sample_distances.get(key)
    return f"🛣️ Distance between {from_city} and {to_city} is {distance} km." if distance else "❌ Distance data not available."

@function_tool
def today_weather(city: str) -> str:
    # Example simulated output
    return f"☀️ Today's weather in {city} is sunny with light breeze."

# ------------------------------------------------------------

# Define two agents for better role management
My_agent_user = Agent(
    name="UserHandler",
    instructions="Handle user input and pass meaningful messages to the main agent.",
    model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp"),
)

My_agent_expert = Agent(
    name="ExpertAgent",
    instructions="Respond with clarity, friendliness, and helpful emojis. Use tools when needed.",
    model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp"),
    tools=[
        calculate_price, web_search, write_note, start_timer,
        add_numbers, give_idea, meditate, check_calendar, listen_music,
        greet_user, convert_temperature, get_motivation, multiplication_table,
        square_number, city_distance, today_weather
    ],
)

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Hello! I am your assistant. How can I help you today? 🤖",
    ).send()

@cl.on_message
async def musadiq(message: cl.Message):
    my_history = cl.user_session.get("history") or []
    my_history.append({"role": "user", "content": message.content})

    # First pass input through user-level agent
    intermediate = await Runner.run(
        starting_agent=My_agent_user,
        input=my_history
    )

    # Append intermediate message and forward to main agent
    my_history.append({"role": "user", "content": intermediate.final_output})

    result = await Runner.run(
        starting_agent=My_agent_expert,
        input=my_history
    )

    my_history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", my_history)

    await cl.Message(
        content=f"Agent Response 🤖 {result.final_output}",
    ).send()
