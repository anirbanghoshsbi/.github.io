# ByteRover Context Curation Knowledge Base

This knowledge base outlines the workflows and technical processes for curating intelligence into a ByteRover Context Tree.

---

## 1. Overview: What is Curation?

Curation is the process of adding, organizing, and maintaining project-specific knowledge.

ByteRover uses **semantic understanding** (not just keyword matching) to:
- Detect domains automatically  
- Prevent duplication  
- Structure information into a navigable hierarchy  

---

## The Curation Lifecycle

1. **Domain Detection**  
   Identifies relevant areas (e.g., `code_style`, `testing`, `infrastructure`)

2. **Duplicate Search**  
   Scans the existing context tree for related knowledge

3. **Action Decision**  
   Decides whether to:
   - Create a new topic  
   - Update an existing one  

4. **Hierarchical Organization**  
   Structures knowledge as:

domain → topic → subtopic

5. **Relation Mapping**  
Creates references like:

@domain/topic

to build a connected knowledge graph

---

## 2. Curation Methods

### A. Via Coding Agents (Cursor, Claude Code, etc.)

The most seamless method.

- Mention **"ByteRover"** in your prompt  
- The agent executes curation automatically  

**Example:**

Work on the task below and update the context tree accordingly: [Task Details]

---

### B. Via REPL or CLI

For manual control:

#### REPL

/curate "missing context about the authentication flow"

#### CLI

brv curate "Topic description" -f path/to/file.ts

---

## 3. Curation Inputs

### File References

Provide grounding context using files.

- **Limit:** Max 5 files per curation  
- **Syntax:**
  - REPL → `@file`
  - CLI → `-f` or `--files`

- **Supported Types:**
  - Code (30+ languages)
  - JSON / YAML
  - Markdown
  - PDF (≤ 50 pages)
  - Office files (`.docx`, `.xlsx`)

---

### Folder Curation

Analyze entire directories.

- Respects `.gitignore`
- Packs folder into structured representation

#### CLI

brv curate -d src/auth

#### REPL

/curate @src/auth/

---

## 4. Automatic Facts Extraction

ByteRover extracts **verifiable statements** into a `## Facts` section.

| Category     | Example |
|--------------|--------|
| Convention   | Use 2-space indentation for all TypeScript files |
| Project      | Token pairs are stored in the database for revocation tracking |
| Environment  | Team uses PostgreSQL 15 for persistence |
| Personal     | Prefers functional components over class components |
| Team         | Code reviews require 2 approvals before merge |

---

## 5. Advanced Curation Strategies

Control how knowledge is stored by specifying **intent**:

### Granular (Breaking Down)
- Splits content into small, reusable units  
- Best for modular knowledge  

### Cohesive (Keeping Together)
- Keeps content as a single topic  
- Best for complex systems  

### Condensed (Summarizing)
- Stores summarized versions  
- Reduces noise and improves clarity  

### Mix & Match
- Apply different strategies per domain  

---

## Key Insight

Curation is not just storage — it's **structured intelligence building**.

Done right, your context tree becomes:
- A memory system  
- A reasoning aid  
- A decision support layer