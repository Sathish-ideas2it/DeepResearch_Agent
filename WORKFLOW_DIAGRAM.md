# Deep Research Agent - Visual Workflow Diagram

## 🔄 Complete System Flow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           DEEP RESEARCH AGENT WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────────┘

📝 INPUT: "Muscle building and healthy lifestyle"

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PHASE 1: STRATEGIC PLANNING                        │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Report        │    │   Query         │    │   Web Search    │    │   Section       │
│   Planner       │───▶│   Generator     │───▶│   (Tavily API)  │───▶│   Planner       │
│   Agent         │    │   (8 queries)   │    │   (Parallel)    │    │   Agent         │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                                                                      │
         │                                                                      ▼
         │                                                          ┌─────────────────┐
         │                                                          │   Report        │
         │                                                          │   Structure     │
         │                                                          │   Generated     │
         │                                                          └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PHASE 2: PARALLEL CONTENT CREATION                │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Section       │    │   Section       │    │   Section       │    │   Section       │
│   Builder       │    │   Builder       │    │   Builder       │    │   Builder       │
│   (Nutrition)   │    │   (Training)    │    │   (Recovery)    │    │   (Supplements)│
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Query Gen     │    │   Query Gen     │    │   Query Gen     │    │   Query Gen     │
│   (5 queries)   │    │   (5 queries)   │    │   (5 queries)   │    │   (5 queries)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Search    │    │   Web Search    │    │   Web Search    │    │   Web Search    │
│   (Parallel)    │    │   (Parallel)    │    │   (Parallel)    │    │   (Parallel)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Content       │    │   Content       │    │   Content       │    │   Content       │
│   Writer        │    │   Writer        │    │   Writer        │    │   Writer        │
│   (150-200w)    │    │   (150-200w)    │    │   (150-200w)    │    │   (150-200w)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         └───────────────────────┼───────────────────────┼───────────────────────┘
                                 │                       │
                                 ▼                       ▼
                    ┌─────────────────────────────────────────┐
                    │         COMPLETED SECTIONS              │
                    │         (Research-based)                │
                    └─────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PHASE 3: FINAL ASSEMBLY                           │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Context       │    │   Introduction  │    │   Conclusion    │    │   Report        │
│   Formatter     │───▶│   Writer        │    │   Writer        │───▶│   Compiler      │
│                 │    │   (50-100w)     │    │   (100-150w)    │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         └───────────────────────┼───────────────────────┘                       │
                                 │                                               │
                                 ▼                                               ▼
                    ┌─────────────────────────────────────────┐    ┌─────────────────┐
                    │         ALL SECTIONS COMPLETE           │    │   Final Report  │
                    │                                         │    │   (Markdown)    │
                    └─────────────────────────────────────────┘    └─────────────────┘
                                                                           │
                                                                           ▼
                                                                  ┌─────────────────┐
                                                                  │   Output File   │
                                                                  │   (final_output.md)│
                                                                  └─────────────────┘
```

## 🏗️ Architecture Layers

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PRESENTATION LAYER                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│  main.py                    │  CLI Interface & Entry Point                     │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              APPLICATION LAYER                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│  workflows/                  │  LangGraph Workflow Orchestration                │
│  ├── main_workflow.py        │  - Main report generation workflow              │
│  └── section_workflow.py     │  - Individual section processing workflow       │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              BUSINESS LOGIC LAYER                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  agents/                     │  Specialized AI Agents                          │
│  ├── report_planner.py       │  - Strategic planning & section creation        │
│  ├── section_builder.py      │  - Research & content generation                │
│  ├── final_section_writer.py │  - Introduction & conclusion writing            │
│  ├── report_compiler.py      │  - Final report assembly                        │
│  ├── runner.py               │  - Execution orchestration                      │
│  └── prompts.py              │  - AI prompt templates                          │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              INFRASTRUCTURE LAYER                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  utils/                     │  Utility Functions                               │
│  ├── search.py              │  - Web search abstraction (Tavily API)          │
│  └── formatters.py          │  - Text processing & formatting                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              DATA LAYER                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│  models/                     │  Data Models & Schemas                          │
│  └── schemas.py              │  - Pydantic models for validation               │
│                              │  - TypedDict for state management               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## 🔄 State Flow Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   ReportState   │    │   SectionState  │    │   SectionState  │
│                 │    │                 │    │                 │
│ topic: str      │    │ section: Section│    │ section: Section│
│ sections: []    │───▶│ search_queries: │───▶│ source_str: str │
│ completed: []   │    │ []              │    │                 │
│ research: ""    │    │                 │    │                 │
│ final: ""       │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       ▼
         │              ┌─────────────────┐    ┌─────────────────┐
         │              │   Query         │    │   Web Search    │
         │              │   Generation    │    │   Execution     │
         │              └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       ▼
         │              ┌─────────────────┐    ┌─────────────────┐
         │              │   Search        │    │   Content       │
         │              │   Results       │    │   Writing       │
         │              └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       └───────┬───────────────┘
         │                               ▼
         │              ┌─────────────────┐
         │              │   Completed     │
         │              │   Section       │
         │              └─────────────────┘
         │                       │
         └───────────────────────┼─────────────────────────────┐
                                 ▼                             │
                    ┌─────────────────┐                        │
                    │   All Sections  │                        │
                    │   Complete      │                        │
                    └─────────────────┘                        │
                                 │                             │
                                 ▼                             │
                    ┌─────────────────┐                        │
                    │   Final Report  │◀───────────────────────┘
                    │   Generation    │
                    └─────────────────┘
```

## 🚀 Performance Characteristics

### Parallel Processing Benefits:
- **4x Faster**: Multiple sections processed simultaneously
- **Resource Efficient**: Async operations prevent blocking
- **Scalable**: Easy to add more parallel workers

### Memory Management:
- **Streaming**: Large content processed in chunks
- **Token Limits**: Smart truncation prevents overflow
- **Cleanup**: Proper resource disposal

### Error Handling:
- **Graceful Degradation**: Continues if some searches fail
- **Retry Logic**: Automatic retry for transient failures
- **Logging**: Comprehensive error tracking

## 🎯 Key Interview Points

1. **"I designed a multi-agent system using LangGraph for orchestration"**
   - Explain how different agents handle different responsibilities
   - Show how LangGraph manages complex workflows

2. **"Implemented parallel processing to improve performance by 3-4x"**
   - Demonstrate async/await usage
   - Show concurrent web searches and content writing

3. **"Used clean architecture principles for maintainability"**
   - Explain separation of concerns
   - Show modular design benefits

4. **"Handled complex state management across async operations"**
   - Explain TypedDict usage
   - Show how state flows through the system

5. **"Implemented production-ready error handling and logging"**
   - Show comprehensive exception handling
   - Explain graceful degradation strategies
