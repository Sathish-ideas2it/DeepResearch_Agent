"""
Main LangGraph workflow for the deep research agent.
"""
from langgraph.graph import StateGraph, START, END
from langgraph.constants import Send

from src.models.schemas import (
    ReportState, 
    ReportStateInput, 
    ReportStateOutput, 
    Section
)
from src.agents.report_planner import generate_report_plan
from src.agents.report_compiler import format_completed_sections, compile_final_report
from src.agents.final_section_writer import write_final_sections
from src.workflows.section_workflow import create_section_workflow


def parallelize_section_writing(state: ReportState):
    """This is the "map" step when we kick off web research for some sections of the report in parallel and then write the section"""
    # Kick off section writing in parallel via Send() API for any sections that require research
    return [
        Send("section_builder_with_web_search",  # name of the subagent node
             {"section": s})
        for s in state["sections"]
        if s.research
    ]


def parallelize_final_section_writing(state: ReportState):
    """Write any final sections using the Send API to parallelize the process"""
    # Kick off section writing in parallel via Send() API for any sections that do not require research
    return [
        Send("write_final_sections",
             {"section": s, "report_sections_from_research": state["report_sections_from_research"]})
        for s in state["sections"]
        if not s.research
    ]


def create_main_workflow():
    """Create the main report generation workflow."""
    builder = StateGraph(ReportState, input=ReportStateInput, output=ReportStateOutput)

    # Get the section builder subagent
    section_builder_subagent = create_section_workflow()

    builder.add_node("generate_report_plan", generate_report_plan)
    builder.add_node("section_builder_with_web_search", section_builder_subagent)
    builder.add_node("format_completed_sections", format_completed_sections)
    builder.add_node("write_final_sections", write_final_sections)
    builder.add_node("compile_final_report", compile_final_report)

    builder.add_edge(START, "generate_report_plan")
    builder.add_conditional_edges("generate_report_plan",
                                  parallelize_section_writing,
                                  ["section_builder_with_web_search"])
    builder.add_edge("section_builder_with_web_search", "format_completed_sections")
    builder.add_conditional_edges("format_completed_sections",
                                  parallelize_final_section_writing,
                                  ["write_final_sections"])
    builder.add_edge("write_final_sections", "compile_final_report")
    builder.add_edge("compile_final_report", END)

    return builder.compile()
