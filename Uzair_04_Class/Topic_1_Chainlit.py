import chainlit as cl
#from Uzair_04_Class.Topic_2_Agent_openroutre import create_agent
from Topic_3_Agent_litellm import agent_creator
import asyncio
@cl.on_chat_start
async def chat_start():
    cl.user_session.set("chat_history", [])
    await cl.Message("welcome",).send()

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("chat_history") or []
    # if history is None:
    #     history = []
    #     cl.user_session.set("History", history)

    user_query = message.content

    history.append({"role":"user", "content": user_query})
    response = asyncio.run(agent_creator(history))

    history.append({"role": "assistant", "content": response})

    await cl.Message(
        content=f"{response}",).send()
    









































































# from chainlit.types import ThreadDict
# from chainlit.types import Message
# from chainlit.types import UserMessage
# from chainlit.types import AssistantMessage
# from chainlit.types import SystemMessage
# from chainlit.types import ErrorMessage
# from chainlit.types import FileMessage
# from chainlit.types import CodeMessage
# from chainlit.types import ImageMessage
# from chainlit.types import VideoMessage
# from chainlit.types import AudioMessage
# from chainlit.types import DocumentMessage
# from chainlit.types import LinkMessage
# from chainlit.types import ButtonMessage
# from chainlit.types import MarkdownMessage
# from chainlit.types import TextMessage
# from chainlit.types import TextAreaMessage
# from chainlit.types import TextInputMessage
# from chainlit.types import TextAreaInputMessage
# from chainlit.types import TextInput
# from chainlit.types import TextAreaInput
# from chainlit.types import TextInputType
# from chainlit.types import TextAreaInputType
# from chainlit.types import TextInputTypeEnum

