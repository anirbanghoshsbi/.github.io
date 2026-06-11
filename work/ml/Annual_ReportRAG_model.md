Given everything you've built and your stated goal (annual reports → company understanding → economic reasoning → investment research), I would **not** build a generic RAG.

I would build this:

# Final Architecture v1.0

```text
Annual Report PDF
        ↓
Page Extraction
        ↓
Page Metadata Enrichment
        ↓
Semantic Chunking
        ↓
Ontology Linking
        ↓
Concept Filtering
        ↓
Metadata Enrichment
        ↓
Concept → Chunk Index
        ↓
Page Summaries
        ↓
Embeddings
        ↓
Qdrant
```

Store four collections:

```text
1. chunks
2. page_summaries
3. concepts
4. relationships (JSON)
```

---

# Ingestion Pipeline

## Layer 1: Page Layer

Keep pages as first-class objects.

```json
{
  "page": 47,
  "company": "HUL",
  "year": 2025,
  "text": "..."
}
```

Reason:

* Natural PDF boundary
* Easy navigation
* Easy citations

---

## Layer 2: Chunk Layer

Your current pipeline.

```text
Page Text
      ↓
Semantic Chunks
```

Example:

```json
{
  "chunk_id": "hul_2025_342",
  "page": 47
}
```

---

## Layer 3: Ontology Layer

You already have:

```text
Controlled Vocabulary
      ↓
Gemma Linking
```

Result:

```json
{
  "chunk_id": "hul_2025_342",
  "concepts": [
      "Pricing Power",
      "Brand Strength",
      "Premiumization"
  ]
}
```

---

## Layer 4: Concept Index

You already plan to build:

```json
{
  "Pricing Power": [
      "chunk_123",
      "chunk_456"
  ]
}
```

Keep it.

This becomes the backbone of future reasoning.

---

## Layer 5: Page Summary Layer

For every page:

```json
{
  "page": 47,
  "summary":
  "Revenue growth driven by premiumization and rural demand recovery."
}
```

Embed summaries.

Store separately.

---

# Storage Architecture

### Collection 1

```text
chunk_collection
```

Contains:

```text
Chunks
Embeddings
Metadata
Concepts
```

---

### Collection 2

```text
page_summary_collection
```

Contains:

```text
Page Summaries
Embeddings
Page Numbers
```

---

### Collection 3

```text
concept_collection
```

Contains:

```text
Controlled Vocabulary
Aliases
Descriptions
Parent Concepts
```

---

### File

```text
concept_relationships.json
```

Contains:

```json
{
  "source": "Brand Strength",
  "relation": "supports",
  "target": "Pricing Power"
}
```

---

# Retrieval Pipeline

Question:

```text
Why are HUL margins improving?
```

---

## Step 1

Ontology Detection

Question →

```text
Margins
Pricing Power
Commodity Costs
Operating Leverage
```

---

## Step 2

Concept Expansion

```text
Margins
      ↓
Pricing Power
      ↓
Brand Strength
```

using:

```text
concept_relationships.json
```

---

## Step 3

Search Page Summaries

Retrieve:

```text
Page 47
Page 48
Page 49
```

---

## Step 4

Search Chunks

Only within:

```text
Pages 47-49
```

This massively improves precision.

---

## Step 5

Retrieve Evidence

```text
Relevant Chunks
```

---

## Step 6

LLM Answer

Context contains:

```text
Page Summaries
+
Relevant Chunks
+
Concept Context
```

---

# What I Would NOT Build Right Now

❌ Neo4j

❌ LangGraph

❌ Agent Swarms

❌ Section Detection Engine

❌ Complex Parent-Child Hierarchies

❌ Multi-agent Retrieval

❌ Knowledge Graph Database

---

# What I Would Build Next

After this architecture works:

```text
Concept Relationships
        ↓
Concept Expansion Retrieval
        ↓
Concept Summaries
        ↓
Multi-Hop Retrieval
```

Example:

```text
Brand Strength
      ↓
Pricing Power
      ↓
Margins
```

Now the system starts reasoning.

---

# The Architecture I Would Personally Use For Your Project

```text
Annual Report
        ↓
Page Extraction
        ↓
Page Summaries
        ↓
Semantic Chunks
        ↓
Ontology Linking
        ↓
Concept → Chunk Index
        ↓
Concept Relationships
        ↓
Embeddings
        ↓
Qdrant
        ↓
Hybrid Retrieval

Query
        ↓
Concept Detection
        ↓
Concept Expansion
        ↓
Page Summary Retrieval
        ↓
Chunk Retrieval
        ↓
Evidence Synthesis
        ↓
Answer
```

This is realistic for a solo builder, leverages the ontology work you've already completed, avoids the PDF section-extraction rabbit hole, and creates a direct path toward the concept-centric economic reasoning system you ultimately want.
