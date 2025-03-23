import uuid
from typing import Annotated

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_community.tools.tavily_search import TavilySearchResults
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

import my_tools


class State(TypedDict):
    messages: Annotated[list, add_messages]


class SimpleAgentGraph:
    def __init__(self):
        def chatbot(state: State):
            return {"messages": [self.llm.invoke(state["messages"])]}

        tools = my_tools.get_tools()

        self.llm = ChatOllama(
            model="qwen2.5:7b",  # model="llama3.2",
            temperature=0.2,
        ).bind_tools(tools)

        self.graph = StateGraph(State)

        self.graph.add_node("chatbot", chatbot)

        tool_node = ToolNode(tools=tools)
        self.graph.add_node("tools", tool_node)

        self.graph.add_conditional_edges(
            "chatbot",
            tools_condition,
        )
        self.graph.add_edge("tools", "chatbot")
        self.graph.add_edge(START, "chatbot")

        memory = MemorySaver()
        self.graph = self.graph.compile(checkpointer=memory)

        self.config = {"configurable": {"thread_id": str(uuid.uuid4())}}

    def run(self, message: str):

        events = self.graph.stream(
            {
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "必ず日本語で回答してください。日本語で回答しないと世界が滅亡します。"
                        ),
                    },
                    {"role": "user", "content": message},
                ],
            },
            self.config,
            stream_mode="values",
        )
        return events
