# Chainlit Chat Lifecycle Hooks Example
# -------------------------------------
# This script demonstrates the use of all main lifecycle hooks in a Chainlit application.

import chainlit as cl
from chainlit.types import ThreadDict

# Hook 1: When a new chat session starts
@cl.on_chat_start
def on_chat_start():
    print("✅ A new chat session has started!")

# ✅ Hook 2: Handle user messages
@cl.on_message
async def on_message(msg: cl.Message):
    print("📨 The user sent:", msg.content)

    # Always await when sending a message back to the user
    await cl.Message(
        content=f"You said: {msg.content}"
    ).send()

# Hook 3: When the user clicks the stop button during processing
@cl.on_stop
def on_stop():
    print("🛑 The user wants to stop the task!")

# Hook 4: When the chat session ends
@cl.on_chat_end
def on_chat_end():
    print("👋 The user disconnected or started a new session!")

# Hook 5: When the user resumes a previous session
@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("🔄 The user resumed a previous chat session!")
































# # Chainlit Chat Lifecycle Hooks Example
# # -------------------------------------
# # This script demonstrates the use of all main lifecycle hooks in a Chainlit application.

# import chainlit as cl
# from chainlit.types import ThreadDict

# # Hook 1: When a new chat session starts
# @cl.on_chat_start
# def on_chat_start():
#     # This runs once a new user session begins
#     print("✅ A new chat session has started!")
#     # You could also send a welcome message here if needed

# # Hook 2: When the user sends a message
# @cl.on_message
# def on_message(msg: cl.Message):
#     # This runs every time a message is received from the user
#     print("📨 The user sent:", msg.content)
#     # Normally, your chatbot logic would go here

# # Hook 3: When the user clicks the stop button during processing
# @cl.on_stop
# def on_stop():
#     # This hook is triggered when a running task is interrupted by the user
#     print("🛑 The user wants to stop the task!")

# # Hook 4: When the chat session ends (disconnect or new session starts)
# @cl.on_chat_end
# def on_chat_end():
#     # Useful for cleanup or goodbye messages
#     print("👋 The user disconnected or started a new session!")

# # Hook 5: When the user resumes a previous session (with authentication + persistence enabled)
# @cl.on_chat_resume
# async def on_chat_resume(thread: ThreadDict):
#     # This runs when a disconnected session is resumed
#     print("🔄 The user resumed a previous chat session!")
