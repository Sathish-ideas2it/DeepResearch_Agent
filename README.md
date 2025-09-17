# Deep Research Agent

A production-ready agentic AI system that analyzes user topics, performs web research, and generates comprehensive technical reports using parallel processing and LangGraph workflows.

## Features

- **Intelligent Report Planning**: Analyzes topics and creates structured report outlines
- **Parallel Web Research**: Performs concurrent web searches for multiple sections
- **Parallel Content Writing**: Generates report sections simultaneously for efficiency
- **Smart Section Management**: Handles research vs. non-research sections differently
- **Professional Formatting**: Produces well-formatted markdown reports with proper citations

## Project Structure

```
├── src/
│   ├── agents/           # Agent functions and workflows
│   │   ├── prompts.py    # Prompt templates
│   │   ├── report_planner.py    # Report planning logic
│   │   ├── section_builder.py   # Individual section processing
│   │   ├── final_section_writer.py  # Introduction/conclusion writing
│   │   ├── report_compiler.py   # Report compilation
│   │   └── runner.py     # Main execution runner
│   ├── models/           # Data models and schemas
│   │   └── schemas.py    # Pydantic models and TypedDict definitions
│   ├── utils/            # Utility functions
│   │   ├── search.py     # Web search functionality
│   │   └── formatters.py # Text formatting utilities
│   └── workflows/        # LangGraph workflow definitions
│       ├── section_workflow.py  # Individual section processing workflow
│       └── main_workflow.py     # Main report generation workflow
├── config/               # Configuration files
├── tests/                # Test files
├── main.py              # Main entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## Usage

### Basic Usage

```python
import asyncio
from src.agents.runner import run_research_agent

async def main():
    topic = "Your research topic here"
    result = await run_research_agent(topic=topic)
    print(result)

asyncio.run(main())
```

### Command Line Usage

```bash
python main.py
```

## Configuration

The agent requires the following environment variables:

- `OPENAI_KEY`: Your OpenAI API key
- `TAVILY_API_KEY`: Your Tavily search API key

## Workflow

1. **Topic Analysis**: The agent analyzes the input topic and generates search queries
2. **Report Planning**: Creates a structured report outline with sections
3. **Parallel Research**: Performs web searches for sections requiring research
4. **Parallel Writing**: Generates content for research-based sections
5. **Final Sections**: Writes introduction and conclusion based on completed sections
6. **Report Compilation**: Combines all sections into a final formatted report

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Structure

- **Models**: Pydantic models for data validation and serialization
- **Agents**: Individual agent functions for specific tasks
- **Workflows**: LangGraph workflow definitions for orchestration
- **Utils**: Reusable utility functions for search and formatting

## License

This project is licensed under the MIT License.
