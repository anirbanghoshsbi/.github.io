# ByteRover Wiki: Querying the Context Tree

This knowledge base provides a structured overview of the **ByteRover Query Context system**, detailing how users and agents interact with the Context Tree.

---

## 1. Overview

ByteRover enables users and autonomous agents to retrieve stored knowledge from a **Context Tree** — a hierarchical, file-based structure located at:

.brv/context-tree/

This structure organizes information into **domains** and **topics**.

Querying is powered by **agentic search**, which:
- Synthesizes information  
- Connects related knowledge  
- Returns answers (not just documents)  

---

## 2. Interaction Methods

Two primary ways to query the Context Tree:

| Method      | Interface            | Best For |
|------------|---------------------|----------|
| `/query`   | ByteRover REPL      | Quick, manual lookups and exploration |
| `brv query`| Coding Agents (e.g., Cursor) | Complex workflows where results feed into code generation |

---

## 3. How Query Works (The 5-Tier Strategy)

ByteRover uses a **multi-tier routing system** to balance speed and intelligence.

It starts from **Tier 0** and escalates only if needed.

### Tier Breakdown

1. **Tier 0: Exact Cache (~0ms)**  
   - Matches identical queries  
   - TTL: 60 seconds  

2. **Tier 1: Fuzzy Cache (~50ms)**  
   - Matches queries with ≥60% token similarity  

3. **Tier 2: BM25 Direct (~100–200ms)**  
   - Full-text search  
   - Skips LLM if confidence is high  

4. **Tier 3: LLM Pre-fetch (<5s)**  
   - Injects top results into a single LLM call  

5. **Tier 4: Agentic Loop (8–15s)**  
   - Multi-step reasoning  
   - Reads files, follows relations, iterates until confident  

---

## 4. Search Intelligence & Ranking

### Compound Scoring Formula

score = (0.6 × BM25 + 0.25 × importance + 0.15 × recency) × tierBoost

#### Components:
- **BM25** → Text relevance  
- **Importance** → Knowledge weight  
- **Recency** → Freshness  
- **Tier Boost** → Priority weighting  

**Tier Boost Rule:**
- "Core" knowledge files → **1.15× boost** over drafts  

---

### Path-Scoped Queries

Narrow search using domain/topic prefixes:

#### Examples:

brv query "auth/jwt refresh token" brv query "authentication refresh token"

---

## 5. Key Features

### Synthesized Answers
- Returns **coherent summaries**
- Includes **citations**
- Avoids dumping raw files  

---

### Relation Following
- Automatically traverses:

@domain/topic

- Builds context across connected knowledge  

---

### Out-of-Domain Detection
- If knowledge is missing:
  - Does **not hallucinate**
  - Suggests **curation of new knowledge**  

---

### Multi-Step Execution
Agents can chain queries:

1. Query Express setup


2. Query TypeScript patterns


3. Combine results into implementation



---

## 6. Best Practices for Queries

### Be Specific
❌ `server stuff`  
✅ `Express health check endpoint with TypeScript`

---

### Include Technical Patterns
- Mention frameworks, protocols, or tools:
  - JWT middleware  
  - Zod schema  
  - OAuth PKCE  

---

### Broad vs Focused Queries

#### For Overview

brv query "authentication"

#### For Implementation

brv query "OAuth PKCE authorization code flow"

---

## Key Insight

Querying in ByteRover is not just retrieval — it's **context synthesis**.

The system:
- Understands intent  
- Navigates structured knowledge  
- Produces actionable, connected answers