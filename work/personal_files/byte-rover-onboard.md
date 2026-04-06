# Wiki Knowledge Base: ByteRover Onboarding Context

This guide outlines the workflow for onboarding existing documentation and context into the ByteRover context tree. This process is optimized for small batches of files (1–3 files) such as READMEs, architecture specs, or security guidelines.

---

## 1. Overview

The **Onboarding Existing Context** workflow allows you to transform static documentation into an intelligent, queryable context tree. ByteRover analyzes the content, detects relevant domains (e.g., compliance, code style), and organizes it hierarchically for use by coding agents.

---

## 2. Prerequisites

Before starting the onboarding process, ensure the following:

- **ByteRover CLI**: Installed and accessible via your terminal  
- **Project Initialization**: The project must be initialized (run `brv` to start the REPL and initialize)  
- **Source Files**: Existing documentation files (Markdown, Code, Config, PDFs, or Office documents)

---

## 3. The Onboarding Workflow

### Step 1: Identify Context Sources

Locate files that contain valuable project knowledge. Common examples include:

- `README.md`  
- `ARCHITECTURE.md`  
- `SECURITY.md`

---

### Step 2: Curate to the Context Tree

Content can be added to the tree using three different methods:

| Method         | Command / Action                                                                 |
|----------------|----------------------------------------------------------------------------------|
| Coding Agent   | Prompt your agent: `"use brv curate to intelligently organize content from [filename]"` |
| Manual CLI     | `brv curate "Description of content" -f [filename]`                              |
| Manual REPL    | Inside the REPL: `/curate "Description of content" @[filename]`                  |

> **Note:** You can reference up to 5 files per curation using the `@` syntax or multiple `-f` flags.

---

### Step 3: Review Changes

To verify how the content was organized and ensure it was added correctly, use the status command:

- CLI: `brv status`  
- REPL: `/status`

This displays added, modified, or deleted files within the `.brv/context-tree/` directory.

---

### Step 4: Query to Verify

Test the retrieval of your new context to ensure the agent can synthesize answers from it:

- CLI: `brv query "your question here"`  
- REPL: `/query your question here`

---

## 4. Technical Mechanics: "Behind the Scenes"

- **Intelligent Curation**: ByteRover automatically detects the domain and creates a hierarchical structure of markdown files in the `.brv/context-tree/` folder  
- **Agentic Search**: When querying, ByteRover reasons about the question, follows relationships between topics, and provides citations from the context  
- **Local Storage**: All context is stored locally by default, making it immediately available for offline queries  

---

## 5. Advanced Options

- **Cloud Sync**: To share context with a team or back it up, use `brv push` (requires a cloud account)  
- **Bulk Extraction**: For entire codebases rather than specific files, use the *Bootstrap from Codebase* workflow instead  

---

## 6. Common Reference Commands

| Command       | Purpose                                      |
|----------------|----------------------------------------------|
| `brv`         | Start the ByteRover REPL                     |
| `brv curate`  | Add context from a string or file            |
| `brv status`  | View the current state of the context tree   |
| `brv query`   | Search the context tree for information      |
| `brv push`    | Sync local context to the cloud              |