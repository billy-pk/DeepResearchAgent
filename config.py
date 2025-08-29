from dotenv import load_dotenv
load_dotenv()
import os

from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from tavily import AsyncTavilyClient
from pydantic import BaseModel

# ---- Model / Client ----
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.5-flash",
)

# search_model = OpenAIChatCompletionsModel(
#     openai_client = external_client,
#     model = "gemini-2.5-flash-lite"
# )

search_model = "gpt-4o"

lead_research_model = OpenAIChatCompletionsModel(
    openai_client = external_client,
    model = "gemini-2.5-flash"
)

# ---- Tavily ----
tavily_client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# ---- Context model ----
class UserInfo(BaseModel):
    name: str
    age: int
    city: str
