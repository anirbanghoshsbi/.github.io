# ByteRover Knowledge Base: Bootstrap & Commands

ByteRover is an agent-native memory architecture that provides a hierarchical **"Context Tree"** for AI coding agents (like Claude Code, Cursor, or Gemini CLI). The Bootstrap workflow is designed to quickly populate this tree by extracting knowledge from an existing codebase.

---

## 1. Core Commands Reference

The ByteRover CLI (`brv`) follows a Git-like mental model for managing agent memory.

| Command            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `brv`             | Starts the interactive TUI/REPL.                                           |
| `brv status`      | Displays the current status of the CLI, background daemon, and project initialization. |
| `brv curate`      | Primary command to analyze and save knowledge to the local Context Tree.   |
| `brv query`       | Searches the Context Tree to retrieve relevant knowledge for a task.       |
| `brv push / pull` | Syncs the local Context Tree with the cloud for team collaboration.        |
| `brv locations`   | Lists registered projects and their associated context tree paths.         |
| `brv providers`   | Manages LLM provider connections (e.g., Anthropic, OpenAI, OpenRouter).    |
| `brv connectors`  | Manages integrations with IDEs and CLI agents (e.g., Cursor, Claude Code). |

---

## 2. Workflow: Bootstrap from Codebase

The **Bootstrap workflow** is the recommended way to initialize memory for a large, existing project. Instead of manual entry, it uses the LLM to scan and structure project-wide information.

### Prerequisites

- **CLI Installed**:  
  ```bash
  npm install -g byterover-cli