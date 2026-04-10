
---

🧠 Hermes Agent — Wiki Knowledge Base

1. Overview

Hermes Agent is a persistent, self-hosted AI agent framework developed by Nous Research.

It represents a shift from:

Stateless AI (chatbots like ChatGPT)
➡️ to

Stateful, continuously learning AI agents


Core Value Proposition

Hermes transforms AI from:

> “a prompt-response tool”



into:

> “a persistent, evolving, autonomous productivity system”




---

2. Key Capabilities

2.1 Persistence & Memory

Remembers all interactions across sessions

Builds long-term, searchable memory

Eliminates need to re-provide context


2.2 Closed Learning Loop

Every completed task → becomes a reusable skill

Every interaction → contributes to knowledge accumulation


2.3 Self-Hosted Architecture

Runs on:

Local machine

Remote server (e.g., DigitalOcean)


Full control over:

Models

Data

Execution environment



2.4 Multi-Platform Access

Accessible via:

Telegram

Discord


Enables remote interaction without being at your system


2.5 Model Agnostic

Can run on any LLM

Not tied to a single provider


2.6 Execution Capabilities

Executes:

Code

Terminal commands


Supports 6 different execution backends


2.7 Skill System

Prebuilt + extensible skills:

Video generation

Writing

Research

Automation




---

3. Conceptual Shift: Chatbot vs Agent

Feature	Chatbots	Hermes Agent

Memory	Stateless	Persistent
Learning	None	Continuous
Context	Session-based	Lifetime
Execution	Limited	Full (code + terminal)
Role	Tool	Autonomous worker


👉 Analogy:

Chatbot = search engine interface

Hermes = employee who learns and improves over time



---

🏗️ Hermes Productivity Stack Architecture

Hermes introduces a 3-layer architecture:


---

Layer 1: Knowledge Layer (LLM-Wiki)

Origin

Concept proposed by Andrej Karpathy

Problem with Traditional LLMs

Operate like RAG systems

Limitations:

Fragmented retrieval

No true knowledge accumulation

Re-discovery instead of memory



LLM-Wiki Solution

A dynamic, structured knowledge system:

Persistent

Interlinked

Continuously growing

Searchable


Functionality

Stores:

Notes

Conversations

Files

Research


Enables:

Cross-referencing

Context inheritance

Knowledge compounding



Mental Model

> A librarian system that:



Files everything

Builds connections

Improves retrieval over time


Hermes Implementation

LLM-Wiki is a built-in skill

Integrated with tools like:

Obsidian



Outcome

Agent gains:

Domain awareness

Historical intelligence

Context continuity




---

Layer 2: Execution Layer (Multi-Agent System)

Introduced In

Hermes update v0.6.0

Core Concept

Multiple specialized agents within one system


---

2.1 Subagents

Independent AI workers

Spawned by main agent

Each assigned a specific task


Examples:

Research agent

Writing agent

Scheduling agent

Email agent



---

2.2 Profiles

Each subagent has:

Separate:

Memory

Sessions

Skills

Configurations

Gateway services



Result

High specialization

Persistent task alignment

No cross-contamination of roles



---

2.3 Knowledge Sharing

All agents:

Access the LLM-Wiki

Start with:

Context

Domain knowledge

User preferences



👉 Eliminates:

Cold starts

Re-learning cycles



---

Example: Marketing Agency System

Main Agent orchestrates:

Agent	Role

Research Agent	Market & client research
Writing Agent	Content creation
Organizer Agent	Scheduling
Email Agent	Client communication


All agents:

Share knowledge layer

Operate independently



---

Layer 3: Output Layer (Execution Results)

Focus

Real-world, high-quality outputs


---

3.1 Manim Skill

Based on:

Manim

Popularized by 3Blue1Brown


Capabilities:

Generate:

Mathematical animations

Technical visualizations


Output:

Clean, high-quality visuals



Use Case:

Explaining complex concepts (e.g., DeFi products)

Enhancing content engagement



---

3.2 Long-Form Content Generation

Example:

Generated:

19 chapters

79,456-word novel


Peer-reviewed using Claude


👉 Demonstrates:

Coherence

Scalability

End-to-end task execution



---

4. System-Level Insight

Traditional AI Workflow

Input → Process → Output → Forget

Hermes Workflow

Input → Process → Output → Store → Learn → Improve → Reuse


---

5. Strategic Importance

Why Hermes Matters

5.1 Fixes AI Architecture Problem

Not just better models

Better system design


5.2 Enables True Productivity Multiplication

Moves beyond:

Prompting


Toward:

Delegation



5.3 Compounding Intelligence

Knowledge grows over time

System becomes:

Faster

Smarter

More aligned




---

6. Key Takeaways

Hermes is not a chatbot, but an agent framework

Built on three layers:

1. Knowledge (LLM-Wiki)


2. Execution (Multi-agent system)


3. Output (Skills & results)



Enables:

Persistent memory

Autonomous workflows

Continuous learning


Represents a shift toward:

> AI as infrastructure, not interface





---

7. Practical Mental Model

Think of Hermes as:

> A digital organization



Knowledge base = Company memory

Agents = Employees

Skills = Tools

You = CEO



---

8. Implementation Direction (Implied)

To fully leverage Hermes:

1. Build LLM-Wiki (Knowledge Base)


2. Define agent roles (Execution Layer)


3. Use skills for output automation


4. Continuously feed and refine system




---
