from agents import Agent, Runner, handoff, RunContextWrapper, set_tracing_disabled 
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
set_tracing_disabled(True)

my_model = LitellmModel(
    api_key=os.getenv("GEMINI_API_KEY"), 
    model="gemini/gemini-2.0-flash-exp",) 

# Creating a handoff
# All agents have a handoffs param, which can either take an Agent directly,
# or a Handoff object that  customizes the Handoff.

urdu_agent = Agent(
    name="Urdu agent",
    instructions="You only speak Urdu.",
    model=my_model
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model=my_model
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[urdu_agent, english_agent],
    model=my_model
)


async def main(input: str):
    result = await Runner.run(starting_agent = triage_agent, input=input,)
    print(result.final_output)

asyncio.run(main("Hello, how are you?"))

#2. Customizing handoffs via the handoff() function

#from agents import Agent, handoff, RunContextWrapper

urdu_agent = Agent(
    name="Urdu agent",
    instructions="You only speak Urdu."
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English"
)

def on_handoff(agent: Agent, ctx: RunContextWrapper[None]):
    agent_name = agent.name
    print("--------------------------------")
    print(f"Handing off to {agent_name}...")
    print("--------------------------------")

    triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    model=my_model,
    handoffs=[
            handoff(urdu_agent, on_handoff=lambda ctx: on_handoff(urdu_agent, ctx)),
            handoff(english_agent, on_handoff=lambda ctx: on_handoff(english_agent, ctx))
    ],
)


async def main1(input: str):
    result = await Runner.run(triage_agent, input=input,)
    print(result.final_output)

asyncio.run(main1("السلام عليكم"))



