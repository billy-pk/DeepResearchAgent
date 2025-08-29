from research_agents import web_search_agent
from synthesis_agent import synthesis_agent
from citation_agent import citation_agent 
from agents import AgentHooks, RunContextWrapper, Agent

tools = [
    web_search_agent.as_tool(
        tool_name = "web_search_tool",
        tool_description = """A tool To efficiently and accurately retrieve information from the web based on 
        the specific search queries and instructions provided by the Planning Agent through lead research agent.
    """
    ),
    synthesis_agent.as_tool(
        tool_name = "synthesis_tool",
        tool_description = """
        You are the Reflection/Synthesis tool, an analytical expert responsible for processing and making sense
         of raw information. Your role is not to just summarize, but to synthesize, analyze, and identify 
        patterns,contradictions, or gaps in the data provided to you.
    """
    ),
    citation_agent.as_tool(
        tool_name = "citation_tool",
        tool_description = """
    To accurately and consistently generate citations for synthesized information based on the source 
    data provided.
    """
    )
]

class CustomAgentHooks(AgentHooks):
    async def on_start(self, wrapper: RunContextWrapper, agent: Agent):
        print(f"[AGENT] {agent.name}  started. ")


    