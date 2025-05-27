# import os
# from dotenv import load_dotenv
# import chainlit as cl
# from litellm import completion
# import json

# # Load the environment variables from the .env file
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# @cl.on_chat_start
# async def start():
#     """Set up the chat session when a user connects."""
#     # Initialize an empty chat history in the session.
#     cl.user_session.set("chat_history", [])

#     await cl.Message(content="Welcome to the Panaversity AI Assistant! How can I help you today?").send()

# @cl.on_message
# async def main(message: cl.Message):
#     """Process incoming messages and generate responses."""
#     # Send a thinking message
#     msg = cl.Message(content="Thinking...")
#     await msg.send()

#     # Retrieve the chat history from the session.
#     history = cl.user_session.get("chat_history") or []
    
#     # Append the user's message to the history.
#     history.append({"role": "user", "content": message.content})
    

#     try:
#         # Get completion from LiteLLM
#         response = completion(
#             model="gemini/gemini-2.0-flash",
#             api_key=gemini_api_key,
#             messages=history
#         )
        
#         response_content = response.choices[0].message.content # type: ignore
        
#         # Update the thinking message with the actual response
#         await msg.update(content=response_content) # type: ignore

#         # Append the assistant's response to the history.
#         history.append({"role": "assistant", "content": response_content})
    
#         # Update the session with the new history.
#         cl.user_session.set("chat_history", history)
        
#         # Optional: Log the interaction
#         print(f"User: {message.content}")
#         print(f"Assistant: {response_content}")
        
#     except Exception as e:
#         msg.content = f"Error: {str(e)}"
#         await msg.update()
#         print(f"Error: {str(e)}")


# # Right on it is not fully functioning because we are not
# # loading json file on on_chat_start
# @cl.on_chat_end
# async def on_chat_end():
#     # Retrieve the full chat history at the end of the session
#     history = cl.user_session.get("chat_history") or []
#     # Save the chat history to a file (or persist it elsewhere)
#     with open("chat_history.json", "w") as f:
#         json.dump(history, f, indent=2)
#     print("Chat history saved.")



import os
import json
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please define it in your .env file.")

# ------------------ Chat Start ------------------ #
@cl.on_chat_start
async def on_chat_start():
    """Initialize chat history when session starts."""
    cl.user_session.set("chat_history", [])
    await cl.Message(content="🌟 Welcome to the Panaversity AI Assistant! How can I help you today?").send()

# ------------------ Message Handler ------------------ #
@cl.on_message
async def on_message(message: cl.Message):
    """Handle user message and generate assistant response."""
    msg = cl.Message(content="🤖 Thinking...")
    await msg.send()

    # Get or initialize chat history
    history = cl.user_session.get("chat_history") or []

    # Add user message to history
    history.append({"role": "user", "content": message.content})

    try:
        # Generate completion
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )
        response_content = response.choices[0].message.content  # type: ignore

        # Update assistant reply and add to history
        await msg.update(content=response_content)
        history.append({"role": "assistant", "content": response_content})

        # Save updated history
        cl.user_session.set("chat_history", history)

        # Log conversation
        print(f"[User]      {message.content}")
        print(f"[Assistant] {response_content}")

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        await msg.update(content=error_msg)
        print(error_msg)

# ------------------ Chat End ------------------ #
@cl.on_chat_end
async def on_chat_end():
    """Save chat history when session ends."""
    history = cl.user_session.get("chat_history") or []
    try:
        with open("chat_history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
        print("✅ Chat history saved to chat_history.json")
    except Exception as e:
        print(f"❌ Failed to save chat history: {str(e)}")
