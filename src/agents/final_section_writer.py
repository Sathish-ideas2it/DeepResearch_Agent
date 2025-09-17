"""
Final section writer for introduction and conclusion sections.
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from src.models.schemas import SectionState
from src.agents.prompts import FINAL_SECTION_WRITER_PROMPT


llm = ChatOpenAI(model_name="gpt-4o", temperature=0)


def write_final_sections(state: SectionState):
    """Write the final sections of the report, which do not require web search and use the completed sections as context"""
    # Get state
    section = state["section"]
    completed_report_sections = state["report_sections_from_research"]

    print('--- Writing Final Section: '+ section.name + ' ---')

    # Format system instructions
    system_instructions = FINAL_SECTION_WRITER_PROMPT.format(
        section_title=section.name,
        section_topic=section.description,
        context=completed_report_sections
    )

    # Generate section
    user_instruction = "Craft a report section based on the provided sources."
    section_content = llm.invoke([
        SystemMessage(content=system_instructions),
        HumanMessage(content=user_instruction)
    ])

    # Write content to section
    section.content = section_content.content

    print('--- Writing Final Section: '+ section.name + ' Completed ---')

    # Write the updated section to completed sections
    return {"completed_sections": [section]}
