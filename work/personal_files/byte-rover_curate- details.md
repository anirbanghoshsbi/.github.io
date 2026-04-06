# ByteRover Wiki: Curation Engine

The **Curation Engine** is the core intelligence layer of ByteRover. It transforms raw data—such as code snippets, conversation logs, and documentation—into a structured, hierarchical **Context Tree**.

Unlike traditional systems that rely on external pipelines, ByteRover follows an **agent-native approach**, where the LLM itself acts as both the architect and librarian of its own memory.

---

## 🧠 Core Philosophy: Agent-Native Memory

The Curation Engine is built on the idea that:

> The same LLM that reasons about a task should also be responsible for storing it.

This eliminates **semantic drift**—a common issue where retrieval systems fail to capture the nuance of stored information.

### 🔁 Key Workflow

1. **Analyze**  
   Examine input for:
   - Architectural decisions  
   - Bug fixes  
   - Recurring patterns  

2. **Reason**  
   Determine placement in the hierarchy:

Domain → Topic → Subtopic

3. **Synthesize**  
- Summarize instead of copy-paste  
- Ensure token efficiency  
- Maintain high information density  

4. **Annotate**  
Add metadata:
- **Provenance** (source of information)  
- **Rationale** (why it matters)  

---

## 🛠️ Curation Mechanisms

The engine provides three primary methods to capture and organize knowledge:

| Method                  | Trigger                     | Purpose                                                                 |
|------------------------|----------------------------|-------------------------------------------------------------------------|
| Active Curation        | `brv curate [path]`        | Manually analyze and onboard files/directories into the Context Tree    |
| Automatic Memory Flush | Context window limit       | Extract key insights before session memory is lost                      |
| Knowledge Mining       | Scheduled (e.g., 9 AM daily) | Identify and extract high-level architectural patterns from sessions |

---

## 📈 Adaptive Knowledge Lifecycle (AKL)

Every entry follows an **Adaptive Knowledge Lifecycle** to prevent clutter and maintain relevance.

### 🔄 Lifecycle Components

- **Maturity Tiers**

Draft → Validated → Core

- **Importance Scoring**  
Assigns priority to entries for retrieval relevance

- **Recency Decay**  
Gradually reduces the weight of outdated or unverified information

---

## 📂 Behind the Scenes

When a curation command is executed, the engine performs automated operations inside:

.brv/context-tree/

### ⚙️ Internal Processes

- **Domain Detection**  
  Automatically categorizes knowledge (e.g., `api-design`, `auth`)

- **Index Propagation**  
  Updates:
  - `_index.md`  
  - `context.md`  
  across hierarchy levels

- **Conflict Resolution**  
  Uses a sequential queue to:
  - Avoid file-level locking  
  - Ensure consistent updates  

---

## 🎥 Research Overview

**ByteRover: Agent-Native Memory Research Paper Overview**

This video explains the technical foundation behind the Curation Engine, showing how agent-led organization achieves higher accuracy than traditional vector database approaches.

> ⚠️ Note: Watching the video will store activity in your YouTube history per YouTube’s Terms of Service.