# ByteRover Wiki: Local Space Structure

ByteRover utilizes an agent-native memory architecture that organizes knowledge into a hierarchical Context Tree. This local space structure is designed to provide persistent, shared memory for AI coding agents without the need for complex vector databases or external fine-tuning.

---

## 🏗️ Context Tree Hierarchy

The knowledge base is organized as a three-level hierarchy stored locally within the `.brv/context-tree/` directory of your project.

| Level     | Description                                                                 | Example Path                                  |
|-----------|-----------------------------------------------------------------------------|-----------------------------------------------|
| Domain    | Top-level folders grouping related knowledge areas. Automatically detected (e.g., `api-design`, `authentication`). | `.brv/context-tree/database/`                 |
| Topic     | Specific subjects within a domain containing core knowledge entries.        | `.../database/query-optimization/`             |
| Subtopic  | *(Optional)* Further granular divisions for complex topics.                 | `.../query-optimization/indexing/`             |

---

## 📂 Key System Files

Alongside curated content, ByteRover maintains several auto-generated files to ensure the tree remains self-describing and navigable.

### 1. `context.md` (Overview Files)
- **Created at:** Each level (Domain, Topic, Subtopic)
- **Purpose:** Documents the scope and purpose of that node
- **Benefit:** Improves human readability and helps agents understand knowledge boundaries

### 2. `_index.md` (Summary Propagation)
- **Generated:** Automatically after each curation
- **Function:** Summarizes the content within a directory
- **Propagation:** Updates cascade upward from subtopic → topic → domain → root

---

## ⚙️ Core Characteristics

- **File-Based Knowledge Graph**  
  Maintains explicit relationships and provenance across entries, unlike flat document stores

- **Adaptive Knowledge Lifecycle (AKL)**  
  Includes:
  - Importance scoring  
  - Maturity tiers  
  - Recency decay  
  → Ensures prioritization of relevant knowledge

- **Local-First & Git-Friendly**  
  Stored within your repository  
  Supports:
  - `brv push`  
  - `brv pull`  
  → Enables seamless team collaboration

- **Agentic Curation**  
  The hierarchy is dynamically maintained by LLM reasoning via:
  ```bash
  brv curate [file]

→ Determines placement or updates existing knowledge automatically


---

🚀 Quick Commands for Local Space

Start REPL & Initialize Workspace

brv

Check Context Tree Status

/status

Curate Content into Tree

/curate [file]



---

🎥 Deep Dive

ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context

This video explains the architecture and research behind the Context Tree, including how hierarchical structuring reduces semantic drift and improves agent accuracy.

> ⚠️ Note: Watching the video will store activity in your YouTube history per YouTube’s Terms of Service.