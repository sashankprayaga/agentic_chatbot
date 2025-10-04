
from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict):
    """State representation for the agentic AI system."""

    messages: Annotated[List, add_messages]