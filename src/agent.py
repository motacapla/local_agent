from uuid import uuid4

from langchain_ollama import OllamaLLM

# from langchain.agents import AgentExecutor, create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
from langchain.prompts import ChatPromptTemplate

from tools import current_datetime

# model = OllamaLLM(
#     model="elyza:jp8b",
#     # model="llama3.2",
#     base_url=f"http://{os.getenv('OLLAMA_HOST')}:11434",
#     temperature=0.7,
# )

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0,
)

# from get_all_tool_names()
usable_default_tool_names = [
    # "wolfram-alpha",
    # "sleep",
    # "google-search",
    "google-search-results-json",
    # # "searx-search-results-json",
    # # "bing-search",
    # # "metaphor-search",
    # # "ddg-search",
    # "google-books",
    # "google-lens",
    # "google-serper",
    # "google-scholar",
    # "google-finance",
    # "google-trends",
    # "google-jobs",
    # "google-serper-results-json",
    # "searchapi",
    # "searchapi-results-json",
    # "serpapi",
    # "dalle-image-generator",
    # "twilio",
    # "merriam-webster",
    # "wikipedia",
    # "arxiv",
    # "golden-query",
    # "pubmed",
    # "human",
    # "awslambda",
    # "stackexchange",
    # "sceneXplain",
    # "graphql",
    # "openweathermap-api",
    # "dataforseo-api-search",
    # "dataforseo-api-search-json",
    # "eleven_labs_text2speech",
    # "google_cloud_texttospeech",
    # "read_file",
    # "reddit_search",
    # "news-api",
    # "tmdb-api",
    # "podcast-api",
    # "memorize",
    # "llm-math",
    # "open-meteo-api",
    # "requests",
    # "requests_get",
    # "requests_post",
    # "requests_patch",
    # "requests_put",
    # "requests_delete",
    # "terminal",
]

tools = [
    *load_tools(usable_default_tool_names),
    TavilySearchResults(
        max_results=3,
        include_answer=True,
        include_raw_content=True,
        include_images=True,
    ),
    # WikipediaQueryRun(
    #     api_wrapper=WikipediaAPIWrapper(
    #         language="ja",
    #         country="jp",
    #     )
    # ),
    Tool.from_function(
        func=current_datetime,
        name="current_datetime",
        description="現在の日付と時刻を取得します",
    ),
]

tool_names = [tool.name for tool in tools] + usable_default_tool_names

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "あなたは優秀なAIアシスタントです。与えられたタスクを解決してください。必要に応じて提供されているツールを使用してください。日本語で回答してください。",
        ),
        ("placeholder", "{messages}"),
    ]
)
memory = MemorySaver()
agent_executor = create_react_agent(
    model=model, tools=tools, prompt=prompt, checkpointer=memory
)
config = {"configurable": {"thread_id": str(uuid4())}}

if __name__ == "__main__":
    user_input = input("Task: ")
    inputs = {"messages": [("user", user_input)]}

    for s in agent_executor.stream(inputs, stream_mode="values", config=config):
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

    # result = agent_executor.invoke({"input": user_input})
    # print("\n最終回答:", result["output"])
