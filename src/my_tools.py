from datetime import datetime
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

from typing_extensions import Annotated


@tool
def current_datetime() -> (
    str
):  # Note: A tool always needs an input and returns an output
    """現在の日時を取得する

    Returns:
        str: 現在の日時
    """
    return datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")


def get_tools():
    return [
        TavilySearchResults(max_results=3),
        current_datetime,
    ]
