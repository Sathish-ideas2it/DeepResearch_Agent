"""
Main runner for the deep research agent.
"""
import asyncio
from IPython.display import display
from rich.markdown import Markdown as RichMarkdown

from src.workflows.main_workflow import create_main_workflow


async def call_planner_agent(agent, prompt, config={"recursion_limit": 50}, verbose=False):
    """Call the planner agent with the given prompt."""
    events = agent.astream(
        {'topic': prompt},
        config,
        stream_mode="values",
    )

    async for event in events:
        for k, v in event.items():
            if verbose:
                if k != "__end__":
                    display(RichMarkdown(repr(k) + ' -> ' + repr(v)))
            if k == 'final_report':
                print('='*50)
                print('Final Report:')
                md = RichMarkdown(v)
                with open("outputs/final_output.md", "w", encoding="utf-8") as f:
                    f.write(v)
                display(md)


async def run_research_agent(topic: str, verbose: bool = False):
    """Run the deep research agent for the given topic."""
    reporter_agent = create_main_workflow()
    result = await call_planner_agent(agent=reporter_agent, prompt=topic, verbose=verbose)
    return result
