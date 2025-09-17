"""
Pydantic models and data structures for the deep research agent.
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from typing_extensions import TypedDict
import operator
from typing import Annotated


class Section(BaseModel):
    """Represents a section of the report."""
    name: str = Field(
        description="Name for a particular section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )
    research: bool = Field(
        description="Whether to perform web search for this section of the report."
    )
    content: str = Field(
        description="The content for this section."
    )


class Sections(BaseModel):
    """Container for all report sections."""
    sections: List[Section] = Field(
        description="All the Sections of the overall report.",
    )


class SearchQuery(BaseModel):
    """Represents a search query for web search."""
    search_query: str = Field(None, description="Query for web search.")


class Queries(BaseModel):
    """Container for multiple search queries."""
    queries: List[SearchQuery] = Field(
        description="List of web search queries.",
    )


class ReportStateInput(TypedDict):
    """Input state for the report generation workflow."""
    topic: str  # Report topic


class ReportStateOutput(TypedDict):
    """Output state for the report generation workflow."""
    final_report: str  # Final report


class ReportState(TypedDict):
    """Main state for the report generation workflow."""
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[list, operator.add]  # Send() API
    report_sections_from_research: str  # String of any completed sections from research to write final sections
    final_report: str  # Final report


class SectionState(TypedDict):
    """State for individual section processing."""
    section: Section  # Report section
    search_queries: list[SearchQuery]  # List of search queries
    source_str: str  # String of formatted source content from web search
    report_sections_from_research: str  # String of any completed sections from research to write final sections
    completed_sections: list[Section]  # Final key we duplicate in outer state for Send() API


class SectionOutputState(TypedDict):
    """Output state for section processing."""
    completed_sections: list[Section]  # Final key we duplicate in outer state for Send() API
