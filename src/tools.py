from datetime import datetime
from langchain_core.tools import tool


@tool
def current_datetime(
    input: str,
) -> str:  # Note: A tool always needs an input and returns an output
    """Get the current date and time

    Returns:
        str: The current date and time
    """
    return datetime.now().strftime("%A %d %B %Y, %I:%M%p")
