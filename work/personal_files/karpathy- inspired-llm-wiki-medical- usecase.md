This Knowledge Source Wiki organizes the hstack ecosystem—a collection of specialized AI agents designed to transform the often overwhelming healthcare experience into a structured, navigable, and informed journey.
## Overview: What is hstack?
hstack is a suite of tools and agent specialists built for patients, caregivers, and "family health researchers." It moves beyond the "blank slate" of standard LLM interactions by providing pre-built workflows for interpreting results, preparing for doctor visits, and synthesizing medical research.
> The Goal: To provide the kind of clarity you’d get if a battle-hardened ER doc, who also happens to be a patient advocate, spent weeks organizing your specific case into a navigable resource.
> 
## Command & Skill Catalog
The following commands are available within the hstack environment to trigger specific workflows:
| Command | Specialist | Primary Function |
|---|---|---|
| /hstack-discuss-case | ER Doc on Call | Triage: Assessment of "Is this normal or an emergency?" (Red/Yellow/Green). |
| /hstack-understand-results | Results Interpreter | Breaks down labs and diagnoses; separates signal from noise. |
| /hstack-prepare-for-visit | Patient Advocate | Builds appointment agendas, prioritized questions, and terminology lists. |
| /hstack-summarize-research | Latest R&D Scout | Synthesizes cutting-edge research, trials, and actionable intelligence. |
| /hstack-wiki-init | Wiki Architect | Bootstraps a disease-specific Obsidian vault from web sources. |
| /hstack-wiki-ingest | Data Integrator | Processes personal files (notes, labs) and weaves them into the wiki. |
| /hstack-wiki-refresh | Knowledge Updater | Re-researches the landscape to update the wiki with new data. |
| /hstack-wiki-lint | Systems Analyst | Health-checks the wiki for broken links, stale content, or contradictions. |
## The Personal Disease Wiki (Karpathy Pattern)
Inspired by the "LLM Wiki" pattern, hstack builds a living document library in Obsidian that grows with your case.
Core Principles
 * Source-First: The wiki is compiled from real documents (research papers, trial results, patient threads) saved in a raw/ folder, not just hallucinated from training data.
 * Emergent Organization: There is no rigid template; the folder structure evolves naturally based on the content of the sources.
 * Progressive Disclosure: Every folder contains an _index.md summary, allowing both humans and LLMs to navigate without information overload.
 * Data Sovereignty: Personal health documents are never modified. The AI reads the raw source and links back to it for verification.
 * Compounding Explorations: Valuable insights from individual conversations can be saved as new pages, making the wiki smarter over time.
## Agent Personas & "Clinical Separation"
All hstack specialists share a foundational voice: A battle-hardened ER doctor and patient advocate. However, they utilize a unique "Clinical Separation" architecture:
 * Clinical Subagents: Behind the scenes, specialized sub-agents (Triage, Lab Interpreter, Research Analyst) perform unbiased, objective analysis.
 * Empathetic Wrapper: The findings are then delivered by the main specialist with appropriate warmth and anxiety-aware communication.
 * Risk Calibration: Every assessment uses a calibrated framework to determine if a situation is "Green" (monitor), "Yellow" (see a doctor soon), or "Red" (ER immediately).
## Installation & Setup
To integrate hstack into a Claude Code environment:
 * Clone and Install:
   git clone https://github.com/kamens/hstack ~/.claude/skills/hstack && cd ~/.claude/skills/hstack && ./install.sh

 * Initialize: Start a new Claude Code session. The commands (e.g., /hstack-discuss-case) will be available immediately.
 * Development: Requires bun. Use bun run gen:skill-docs to generate new skills from templates.
## Important Disclaimer
hstack is an AI tool, not a medical professional. It is designed to be a "thinking partner" to help you communicate more effectively with your healthcare team.
 * It cannot perform physical exams or run tests.
 * It cannot replace professional medical advice.
 * Always consult a doctor for clinical decisions.
 * In a crisis, contact emergency services immediately.
