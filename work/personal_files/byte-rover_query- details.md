This wiki knowledge base is structured based on the technical documentation for the ByteRover Query Engine, a system designed to provide agent-native memory through a hierarchical "Context Tree."
1. Core Concept: The Query Engine
The Query Engine is the retrieval layer of ByteRover. It allows AI agents and users to extract specific, synthesized knowledge from the local Context Tree. Unlike traditional vector databases that rely purely on similarity scores, ByteRover uses a multi-tier "Agentic Search" strategy to navigate a hierarchical markdown-based file system.
2. Retrieval Architecture (Multi-Tier Strategy)
The engine does not use a single retrieval method. Instead, it routes queries through several tiers to balance speed and accuracy:
 * Tier 1: Exact Caching: Instantly returns results for recurring queries.
 * Tier 2: BM25 Full-Text Search: Uses compound scoring to find relevant keywords within the markdown files.
 * Tier 3: LLM-Assisted Pre-fetch: An LLM identifies which domains or topics are likely to contain the answer.
 * Tier 4: Agentic Reasoning: For complex queries, a "reasoning agent" navigates the tree, following explicit relations (e.g., @domain/topic) to gather connected context.
 * Tier 5: Out-of-Domain Detection: If the information does not exist in the tree, the engine explicitly signals a "cache miss" rather than hallucinating an answer.
3. The Context Tree Structure
Knowledge is stored in the .brv/context-tree/ directory using a human-readable, Git-friendly hierarchy:
 * Domains: Top-level categories (e.g., architecture/, api-design/).
 * Topics: Specific subjects within a domain (e.g., architecture/auth-flow/).
 * Subtopics: Optional deeper nesting for granular details.
 * Entries: The actual .md files containing the knowledge.
Auto-Generated Files:
 * context.md: A self-describing overview generated at each level of the hierarchy.
 * _manifest.json: A registry that tracks the "maturity" and importance of all entries.
4. Key Features & Workflows
| Feature | Description |
|---|---|
| Agentic Search | Replaces Vector DBs; agents "read" and navigate the tree like a developer would. |
| Synthesis | Instead of returning document snippets, the engine reads relevant files and synthesizes a coherent answer with citations. |
| Adaptive Lifecycle | Knowledge is scored by importance and maturity (e.g., Draft → Validated → Core) and is subject to recency decay. |
| Local-First | All queries run against the local filesystem; no external infrastructure or cloud account is required by default. |
5. How to Execute Queries
There are two primary ways to interact with the Query Engine:
 * Manual Lookup (REPL):
   Run /query <your question> directly in the ByteRover REPL for quick information retrieval.
 * Agent Integration (CLI):
   AI coding agents (like Cursor or Claude Code) execute brv query "<your question>" to pull context into their active workspace.
6. Comparison: Vector DB vs. Context Tree
| Aspect | Vector Database (Traditional) | ByteRover Context Tree |
|---|---|---|
| Storage | High-dimensional embeddings | Human-readable Markdown |
| Retrieval | Mathematical similarity (Cosine) | Agentic navigation & Full-text search |
| Transparency | Black box | Fully auditable and editable |
| Infrastructure | Requires DB & Embedding service | Zero infrastructure (Local Files) |
