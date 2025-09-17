"""
Main entry point for the Deep Research Agent.

This is a refactored version of the original main_single.py file,
now organized into a clean, production-ready structure.
"""
import asyncio
from dotenv import load_dotenv
import os

from src.agents.runner import run_research_agent


def setup_environment():
    """Setup environment variables and configuration."""
    # Load .env file
    load_dotenv()
    
    # Set environment variables
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_KEY")
    os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")


async def main():
    """Main function to run the deep research agent."""
    # Setup environment
    setup_environment()
    
    # Define the topic for research
    topic = "Detailed report on key to muscle building and health life style"
    
    # Run the research agent
    result = await run_research_agent(topic=topic, verbose=False)
    print(result)


if __name__ == "__main__":
    # Run the async function
    asyncio.run(main())
