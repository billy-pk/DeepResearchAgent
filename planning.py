from agents import Agent
from config import model
from lead_research_agent import lead_research_agent
from tools import CustomAgentHooks
from agents import ModelSettings


planning_agent = Agent(
    name="Planning Agent",
    instructions="""
You are a helpful planning assistant.  Your goal is to create a comprehensive, multi-stage research plan. Given 
an input from requirement_gathering agent, prepare a set of web searches to best answer the user
requirement/ query. Make  between 5 and 10 terms to query for. After plan creation, you will handoffs to Lead Research Agent.
# IMPORTANT:  you will not respond to user at your own. you will handoff your plan to Lead Research Agent.

 """,
    model=model,
    model_settings = ModelSettings( temperature = 0.2),
    handoff_description= """
You are a planning agent. Your goal is to create a comprehensive, multi-stage research plan. After plan creation, 
you will handoffs to Lead Research Agent. You must not reply to user at your own.
Your plan must be logical, efficient, and directly address all aspects of user's requirements.
""",
handoffs = [lead_research_agent],
hooks = CustomAgentHooks()
)
