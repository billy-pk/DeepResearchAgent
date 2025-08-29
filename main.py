import asyncio
from typing import Any
from agents import Runner, RunHooks
from config import UserInfo
from requirement_gathering import requirement_gathering_agent
from rich import print

# ---- Control flag ----
loop_running = True

# define our CustumRunHooks class which will hook the handoffs and set control flag to false 
class CustomRunHooks(RunHooks):
    async def on_handoff(self, context, from_agent, to_agent):
        global loop_running
        loop_running = False

history = []
async def interactive_main(history: Any):
    context = UserInfo(name="John Doe", age=30, city="New York")  # Example context
    result = await Runner.run(
        requirement_gathering_agent,
        input=history,
        context=context,
        max_turns = 30,
        hooks=CustomRunHooks(),
    )
    print(f"\nAGENT:  Last Agent Name  {result.last_agent.name}  {result.final_output} ")
    history.extend(result.to_input_list())
    return history

if __name__ == "__main__":
    while loop_running:
        user_input = input("YOU: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the assistant.")
            break
        history.append({"role": "user", "content": user_input})
        asyncio.run(interactive_main(history))



