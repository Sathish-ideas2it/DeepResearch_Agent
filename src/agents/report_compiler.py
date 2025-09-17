"""
Report compilation and formatting functions.
"""
from src.models.schemas import ReportState
from src.utils.formatters import format_sections


def format_completed_sections(state: ReportState):
    """Gather completed sections from research and format them as context for writing the final sections"""
    print('--- Formatting Completed Sections ---')

    # List of completed sections
    completed_sections = state["completed_sections"]

    # Format completed section to str to use as context for final sections
    completed_report_sections = format_sections(completed_sections)

    print('--- Formatting Completed Sections is Done ---')

    return {"report_sections_from_research": completed_report_sections}


def compile_final_report(state: ReportState):
    """Compile the final report"""
    # Get sections
    sections = state["sections"]
    completed_sections = {s.name: s.content for s in state["completed_sections"]}

    print('--- Compiling Final Report ---')

    # Update sections with completed content while maintaining original order
    for section in sections:
        section.content = completed_sections[section.name]

    # Compile final report
    all_sections = "\n\n".join([s.content for s in sections])
    # Escape unescaped $ symbols to display properly in Markdown
    formatted_sections = all_sections.replace("\\$", "TEMP_PLACEHOLDER")  # Temporarily mark already escaped $
    formatted_sections = formatted_sections.replace("$", "\\$")  # Escape all $
    formatted_sections = formatted_sections.replace("TEMP_PLACEHOLDER", "\\$")  # Restore originally escaped $

    print('--- Compiling Final Report Done ---')

    return {"final_report": formatted_sections}
