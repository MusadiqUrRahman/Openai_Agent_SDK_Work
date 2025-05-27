# 
#                        ============================================================
#                            Agent with Chainlit & History Integration 🔗🧠📜
#                        ============================================================


import chainlit as cl
from chainlit_agent_02 import agent_creator
from agents import Runner
# from openai.types.responses import ResponseTextDeltaEvent


@cl.on_chat_start
async def start():
    await cl.Message(
        content="✨ Hi! I am Syed, your AI assistant. How can I help you today?✨").send()
    
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat_history", [])

@cl.on_message
async def main(message: cl.Message):
    
    # Retrieve the chat history from the session.
    my_history = cl.user_session.get("chat_history") or []

    # Append the new message to the chat history.
    my_history.append({"role": "user", "content": message.content})
    
    my_agent = agent_creator()

    response = await Runner.run(starting_agent=my_agent, input=my_history)

# # streaming
#     async for event in response.stream_events():
#          if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             print(event.data.delta, end="", flush=True)


    # Append the assistant's response to the chat history.
    my_history.append({"role": "assistant", "content": response.final_output})

    # Update the chat history in the session.
    cl.user_session.set("chat_history", my_history)
  
    await cl.Message(content=f"✨Syed Say This✨: {response.final_output}",).send()

#====================================================================================

