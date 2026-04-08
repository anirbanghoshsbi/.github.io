
---

🧠 DeepTutor Wiki — Agent-Native Personalized Tutoring System


---

1. 🌐 Core Philosophy

1.1 From Chatbot → Agent-Native Tutor

DeepTutor is not a chatbot. It is an agent-native system designed to behave like a persistent, evolving tutor.

Key Paradigm Shift:

Traditional AI	DeepTutor

Stateless chat	Persistent memory
Single LLM	Multi-agent system
Prompt-response	Workflow orchestration
Passive answering	Active teaching


👉 The system introduces:

Autonomous TutorBot

Persistent learning memory

Multi-mode unified workflow 



---

1.2 Unified Learning Loop

DeepTutor creates a closed learning loop:

Learn → Solve → Generate → Research → Reflect → Store → Repeat

Each stage feeds into:

Knowledge Base

Memory

Future interactions


👉 This is critical: learning compounds over time


---

2. 🧩 System Architecture Overview

2.1 High-Level Architecture

Frontend (Next.js)
        ↓
API Layer (FastAPI)
        ↓
Agent Layer (Multi-agent orchestration)
        ↓
Tools Layer (Execution + Retrieval)
        ↓
Knowledge Layer (RAG + Graph)
        ↓
Data Layer (User + KB storage)


---

2.2 Core Layers Explained

🖥️ Frontend Layer

Built using Next.js 16

Acts as the user interaction surface


Capabilities:

Dashboard

Knowledge base management

Problem solving

Question generation

Research workspace

Guided learning

Co-writer editor 


👉 Insight:
Frontend is multi-interface, not chat-only


---

🔌 API Layer

Built with FastAPI, provides:

REST endpoints

WebSocket streaming

Real-time updates

Modular route structure 


👉 Design Insight:

Enables streaming reasoning

Decouples frontend from agents



---

🤖 Agent Layer (Core Intelligence)

This is the brain of DeepTutor.

Agents are specialized, modular, orchestrated.


---

2.3 Key Agents

1. Question Generation Agent

Generates questions from knowledge

Uses structured inputs:

knowledge point

difficulty

context



👉 Important Shift:

No rejection loop

Single-pass generation 



---

2. Relevance Analyzer

Evaluates generated content

Outputs:

relevance level

coverage

extension points



👉 Insight:

Moves from validation → explanation



---

3. Agent Coordinator

Orchestrates multi-agent workflows

Handles:

sequencing

batching

customization



👉 This is your Agent OS layer


---

4. Co-Writer Agents

EditAgent

Rewrite / Expand / Shorten

Uses RAG or web context


NarratorAgent

Converts text → speech (TTS)


👉 Turns system into:

Writing assistant

Teaching narrator 



---

3. 🛠️ Tools Layer (Execution Engine)

This is where DeepTutor becomes agentic (action-capable).

3.1 Core Tools

Tool	Function

Code Executor	Runs Python in sandbox
RAG Tool	Retrieves knowledge
Web Search	External info
Paper Search	Research papers
Tex Tools	Academic parsing





---

3.2 Code Execution System

Features:

Isolated environment

Async + sync execution

Persistent workspace

Secure filesystem


👉 Insight: DeepTutor is not just answering—it can compute, test, and verify


---

4. 📚 Knowledge System (RAG + Graph)

4.1 Knowledge Base Design

DeepTutor uses:

Document ingestion

Knowledge graph storage

Incremental updates



---

4.2 Incremental Knowledge Architecture

Key innovation:

Instead of rebuilding:

Only new documents are processed

Automatically merged into graph


Benefits:

Lower cost

Faster updates

No duplication 



---

4.3 Knowledge Graph Storage

Stored as:

Entities

Relations

Content lists

Extracted items


Example:

Definition
Theorem
Formula
Figures

👉 Insight: This enables:

Structured reasoning

Not just text retrieval



---

4.4 RAG Evolution

DeepTutor’s RAG is:

Persistent

Incremental

Graph-enhanced


👉 This is closer to: Agentic Knowledge Base (AKB) than naive RAG


---

5. 🧠 Memory System

5.1 Persistent Learning Memory

Tracks:

What user learned

Learning style

Goals

Interaction history 



---

5.2 TutorBot Memory

Each TutorBot has:

Independent memory

Personality

Skills


👉 Insight: This is like: Custom fine-tuned agent per user


---

6. 🤖 TutorBot (Core Entity)

6.1 What is TutorBot?

A personal AI tutor agent with:

Memory

Skills

Autonomy

Multi-modal interaction



---

6.2 Capabilities

Reminds user

Learns user behavior

Adapts teaching style

Executes workflows


👉 Important: TutorBot ≠ Chatbot
It is a stateful learning companion


---

7. 🔄 Multi-Mode System (Unified Workspace)

DeepTutor integrates 5 core modes into a single conversation:

Mode	Function

Chat	Basic interaction
Solve	Problem solving
Question	Quiz generation
Research	Deep exploration
Guide	Structured learning


👉 All modes:

Share context

Share memory

Share knowledge 



---

8. ✍️ Co-Writer System

8.1 Purpose

Turn AI into a collaborative writer


---

8.2 Features

Rewrite text

Expand ideas

Compress content

Add context via RAG/web



---

8.3 Output Integration

Saved to notebook

Reused in learning loop


👉 Insight: This closes the loop: Thinking → Writing → Learning


---

9. 🧾 Data Layer

9.1 Directory Structure

data/
├── knowledge_bases/
└── user/
    ├── solve/
    ├── question/
    ├── research/
    ├── co_writer/
    ├── notebook/
    ├── guide/
    └── run_code_workspace/




---

9.2 Data Types

Knowledge Data

Documents

Graph structures


User Data

Solutions

Questions

Notes

Research outputs



---

9.3 Key Insight

Data is:

Modular

Task-specific

Persistent



---

10. 🧠 Guided Learning System

10.1 Concept

Transforms content into:

Step-by-step learning paths

Interactive sequences



---

10.2 Structure

Plan → Steps → Interaction → Reflection


---

10.3 Benefit

Converts passive reading → active learning



---

11. 🔬 Research System

Allows:

Deep exploration

Report generation

Context caching



---

Key Capability:

Multi-source synthesis

Persistent outputs



---

12. 🧪 Execution Workspace

12.1 Code Workspace

Temporary file storage

Execution outputs

Safe environment



---

12.2 Importance

Enables:

Learning by doing

Experimentation



---

13. 🔌 Plugin System (New Architecture)

13.1 Two-Layer Plugin Model

Introduced in v1.0:

Layer 1: Tools

Functional capabilities


Layer 2: Capabilities

Higher-level behaviors





---

13.2 Why Important?

Separates:

Execution → Tools

Intelligence → Capabilities


👉 This is a clean agent abstraction layer


---

14. ⚙️ CLI + SDK

DeepTutor provides:

CLI interface

SDK for developers


Use cases:

Automation

Integration

Custom pipelines



---

15. 🚀 Key Innovations Summary

15.1 What Makes DeepTutor Unique

1. Agent-Native Architecture

Not prompt-based

Workflow-driven



---

2. Persistent Learning Memory

Long-term adaptation



---

3. Unified Learning Workspace

Multi-mode, single context



---

4. Incremental Knowledge Graph

Efficient and scalable



---

5. Tool-Augmented Intelligence

Code + search + reasoning



---

6. TutorBot Concept

Personalized evolving agent



---

16. 🧠 Mental Model (IMPORTANT)

Think of DeepTutor as:

Not = ChatGPT + RAG

But =

(AI Operating System)
        +
(Personal Tutor Agent)
        +
(Knowledge Graph Brain)
        +
(Action Tools)


---

17. 🏗️ How You Can Use This (For Your Goals)

Given your interest in:

Agentic systems

Knowledge bases

Trading ML


👉 DeepTutor teaches you:

1. Build Agent OS

→ Coordinator + Tools + Memory

2. Replace RAG with:

→ Persistent Knowledge Graph

3. Create Specialized Agents:

→ Analyst, Trader, Researcher

4. Add Memory Layer:

→ Your trading journal → agent memory


---

18. ⚡ Final Insight (Most Important)

DeepTutor is not a product.
It is a pattern:

> 👉 “AI becomes useful when it stops answering and starts doing, remembering.