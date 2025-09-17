"""
Section building agent functions for individual report sections.
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from src.models.schemas import SectionState, Queries, SearchQuery
from src.utils.search import run_search_queries
from src.utils.formatters import format_search_query_results
from src.agents.prompts import (
    REPORT_SECTION_QUERY_GENERATOR_PROMPT,
    SECTION_WRITER_PROMPT
)


llm = ChatOpenAI(model_name="gpt-4o", temperature=0)


def generate_queries(state: SectionState):
    """Generate search queries for a specific report section"""
    # Get state
    section = state["section"]
    print('--- Generating Search Queries for Section: '+ section.name +' ---')

    # Get configuration
    number_of_queries = 5

    # Generate queries
    structured_llm = llm.with_structured_output(Queries)

    # Format system instructions
    system_instructions = REPORT_SECTION_QUERY_GENERATOR_PROMPT.format(
        section_topic=section.description,
        number_of_queries=number_of_queries
    )

    # Generate queries
    user_instruction = "Generate search queries on the provided topic."
    search_queries = structured_llm.invoke([
        SystemMessage(content=system_instructions),
        HumanMessage(content=user_instruction)
    ])

    print('--- Generating Search Queries for Section: '+ section.name +' Completed ---')

    return {"search_queries": search_queries.queries}


async def search_web(state: SectionState):
    """Search the web for each query, then return a list of raw sources and a formatted string of sources."""
    # Get state
    search_queries = state["search_queries"]

    print('--- Searching Web for Queries ---')

    # Web search
    query_list = [query.search_query for query in search_queries]
    search_docs = await run_search_queries(search_queries, num_results=6, include_raw_content=True)

    # Deduplicate and format sources
    search_context = format_search_query_results(search_docs, max_tokens=4000, include_raw_content=True)

    print('--- Searching Web for Queries Completed ---')

    return {"source_str": search_context}


def write_section(state: SectionState):
    """Write a section of the report"""
    # Get state
    section = state["section"]
    source_str = state["source_str"]

    print('--- Writing Section : '+ section.name +' ---')

    # Format system instructions
    system_instructions = SECTION_WRITER_PROMPT.format(
        section_title=section.name,
        section_topic=section.description,
        context=source_str
    )

    # Generate section
    user_instruction = "Generate a report section based on the provided sources."
    section_content = llm.invoke([
        SystemMessage(content=system_instructions),
        HumanMessage(content=user_instruction)
    ])

    # Write content to the section object
    section.content = section_content.content

    print('--- Writing Section : '+ section.name +' Completed ---')

    # Write the updated section to completed sections
    return {"completed_sections": [section]}
