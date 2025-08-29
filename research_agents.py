from agents import Agent, ModelSettings, function_tool
from config import search_model, tavily_client

@function_tool
async def web_search(query : str) -> dict: # tavily returns a dict with the search results
    """
    Search the web for the given query and return the results.
    Args:
        query (str) : The query to search for
    Returns:
        response (dict) : The search results from Tavily
        """
    response = await tavily_client.search(query, max_results = 1)
    print("[web search tool called]")
    # for result in response.get("results", []):
    #     #print(result)
    #     print(f" \n\n {result.get('url')}, CONTENT: {result.get('content')}")
    return response


web_search_agent = Agent(
    name = "Web Search Agent",
    instructions = """
You are the Web Search Agent, a specialized component within a deep research system. Given a search term, 
you search the web for that term and produce a concise summary of the results. The summary must be 2-3 
paragraphs and less than 300 words. Capture the main points. Write succinctly, no need to have complete 
sentences or good grammar. This will be consumed by someone synthesizing a report, so its vital you capture 
the essence and ignore any fluff. Do not include any additional commentary other than the summary "
You act as the information retriever, providing relevant data to subsequent processing stages.

""",
    model = search_model,
    tools = [web_search],
    model_settings= ModelSettings(max_tokens= 1000)
    
)
