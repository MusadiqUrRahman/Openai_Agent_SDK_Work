from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv, find_dotenv
import os
import chainlit as cl

load_dotenv(find_dotenv())

set_tracing_disabled(True)

My_agent1 = Agent(
    name="Assistant",
    instructions="You will respond to user query",         
    model=LitellmModel(api_key=os.getenv("GEMINI_API_KEY"), model="gemini/gemini-2.0-flash-exp",) 

    )

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])  # Initialize history
    await cl.Message(
        content="Hello! I am your assistant. How can I help you today? 🤖",
    ).send()

@cl.on_message
async def musadiq(message: cl.Message):
    my_history = cl.user_session.get("history") or []

    # Check if the user asked to see chat history
    if message.content.lower() in ["show history", "ہسٹری دکھاؤ"]:
        if not my_history:
            await cl.Message(content="📭 کوئی ہسٹری موجود نہیں ہے۔").send()
        else:
            history_text = ""
            for msg in my_history:
                role = "👤 User" if msg["role"] == "user" else "🤖 Assistant"
                history_text += f"{role}: {msg['content']}\n\n"

            await cl.Message(content=f"🕘 Chat History:\n\n{history_text}").send()
        return  # Skip rest of processing

    # Normal conversation flow
    my_history.append({"role": "user", "content": message.content})

    result = await Runner.run(
        starting_agent=My_agent1,
        input=my_history,
    )

    my_history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", my_history)

    await cl.Message(
        content=f"Agent Response 🤖 {result.final_output}",
    ).send()
