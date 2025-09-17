"""
Search utilities for web research functionality.
"""
import asyncio
from dataclasses import asdict, dataclass
from typing import List, Dict, Union, Any
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper


@dataclass
class SearchQuery:
    """Search query data class for handling objects created from LLM responses."""
    search_query: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# Initialize Tavily search wrapper lazily to avoid API key validation at import time
tavily_search = None

def get_tavily_search():
    """Get Tavily search wrapper, initializing it if needed."""
    global tavily_search
    if tavily_search is None:
        tavily_search = TavilySearchAPIWrapper()
    return tavily_search


async def run_search_queries(
    search_queries: List[Union[str, SearchQuery]],
    num_results: int = 5,
    include_raw_content: bool = False
) -> List[Dict]:
    """
    Asynchronously run tavily search queries for specific list of queries and return back the search results.
    This is async so it is non blocking and can be executed in parallel.
    """
    search_tasks = []

    for query in search_queries:
        # Handle both string and SearchQuery objects
        # Just in case LLM fails to generate queries as:
        # class SearchQuery(BaseModel):
        #     search_query: str
        query_str = query.search_query if isinstance(query, SearchQuery) else str(query)  # text query

        try:
            # get results from tavily asynchronously (in parallel) for each search query
            search_tasks.append(
                get_tavily_search().raw_results_async(
                    query=query_str,
                    max_results=num_results,
                    search_depth='advanced',
                    include_answer=False,
                    include_raw_content=include_raw_content
                )
            )
        except Exception as e:
            print(f"Error creating search task for query '{query_str}': {e}")
            continue

    # Execute all searches concurrently and await results
    try:
        if not search_tasks:
            return []
        search_docs = await asyncio.gather(*search_tasks, return_exceptions=True)
        # Filter out any exceptions from the results
        valid_results = [
            doc for doc in search_docs
            if not isinstance(doc, Exception)
        ]
        return valid_results
    except Exception as e:
        print(f"Error during search queries: {e}")
        return []
