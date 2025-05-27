import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    #print("A new chat session has started!")

    await cl.Message(content="my name is syed").send()


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Hello: {message.content}",
    ).send() 