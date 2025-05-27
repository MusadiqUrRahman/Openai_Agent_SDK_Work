
import chainlit as cl
from chainlit.types import ThreadDict

# ✅ نیا چیٹ سیشن شروع ہونے پر
@cl.on_chat_start
def on_chat_start():
    print("✅ نیا چیٹ سیشن شروع ہو گیا!")

# 📨 جب یوزر میسج بھیجتا ہے
@cl.on_message
def on_message(msg: cl.Message):
    print("📨 یوزر نے بھیجا:", msg.content)

# 🛑 جب یوزر Stop بٹن دبائے
@cl.on_stop
def on_stop():
    print("🚫 یوزر نے ٹاسک روکنے کی درخواست دی!")

# 🔚 جب چیٹ ختم ہو (disconnect یا نیا سیشن)
@cl.on_chat_end
def on_chat_end():
    print("👋 یوزر نے چیٹ ختم کر دی یا نیا چیٹ سیشن شروع کر دیا!")

# 🔁 جب یوزر پرانا سیشن دوبارہ کھولے (authentication enabled ہو تو)
@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("🔄 یوزر نے پرانا سیشن دوبارہ شروع کیا!")
