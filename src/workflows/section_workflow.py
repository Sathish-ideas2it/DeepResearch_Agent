"""
LangGraph workflow for individual section processing.
"""
from langgraph.graph import StateGraph, START, END
from langgraph.constants import Send

from src.models.schemas import SectionState, SectionOutputState
from src.agents.section_builder import generate_queries, search_web, write_section


def create_section_workflow():
    """Create the section processing workflow."""
    # Add nodes and edges
    section_builder = StateGraph(SectionState, output=SectionOutputState)
    section_builder.add_node("generate_queries", generate_queries)
    section_builder.add_node("search_web", search_web)
    section_builder.add_node("write_section", write_section)

    section_builder.add_edge(START, "generate_queries")
    section_builder.add_edge("generate_queries", "search_web")
    section_builder.add_edge("search_web", "write_section")
    section_builder.add_edge("write_section", END)
    
    return section_builder.compile()
