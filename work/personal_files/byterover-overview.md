To make this easy to copy, I have wrapped the entire Wiki content in a single code block below. You can copy the code directly into a file named byterover-wiki.md.
# ByteRover Wiki

## 1. Overview
ByteRover is a **local-first AI context engineering** platform designed for coding agents. It provides these agents with "persistent memory" by storing project knowledge locally on your machine.

* **Primary Goal:** To give AI tools (like Cursor, Claude Code, or Windsurf) a better understanding of your codebase without requiring a cloud-heavy infrastructure.
* **Privacy Model:** Everything works offline by default. You can "Bring Your Own Key" (BYOK) for LLM providers, meaning no ByteRover account is strictly necessary for core functionality.

> **Clarity Note: Context Engineering** > Context engineering refers to the process of organizing and refining the information (code, docs, history) provided to an AI model so it can give more accurate and relevant answers. Instead of giving the AI a messy pile of files, ByteRover structures that data so the AI "knows" where to look.

---

## 2. Core Concepts

### Context Tree
The Context Tree is your project’s knowledge base.
* **Storage:** Saved as human-readable Markdown files in `.brv/context-tree/`.
* **Organization:** Hierarchically organized by domain and topic.
* **Git-Friendly:** Because it is just Markdown, you can commit it to your repository to share context with your team.

### LLM Providers
ByteRover supports 18+ external providers, including:
* OpenRouter, Anthropic, OpenAI.
* Local models (run on your own hardware).
* A built-in LLM (requires a free ByteRover account).

> **Clarity Note: BYOK (Bring Your Own Key)** > This means you use your existing subscription/API key from a provider like OpenAI. ByteRover acts as the "bridge" rather than a middleman that charges you for the AI usage itself.

### Daemon-First Architecture
The system runs a background **daemon** that handles all heavy lifting.
* **No manual start:** It auto-starts when you run a command.
* **Connectivity:** Both the CLI and coding agents connect to this single daemon for a consistent state.

> **Clarity Note: Daemon** > A "daemon" is a background process that runs without a user interface. In ByteRover's case, it ensures that if you change a setting in your terminal, your AI agent in VS Code immediately knows about it.

### BRV Hub
A community marketplace where users can find and install pre-built agent skills and context bundles.

---

## 3. Getting Started

### Installation
You can install the ByteRover CLI using one of the following methods:

**Option A: Shell Script (macOS/Linux)**
```bash
curl -fsSL [https://byterover.dev/install.sh](https://byterover.dev/install.sh) | sh

Option B: NPM (Cross-platform/Windows)
Requires Node.js 20+
npm install -g byterover-cli

Initial Setup
 * Open your project:
   cd path/to/your/project
brv

   This opens the TUI (Terminal User Interface).
 * Connect a Provider:
   To use your own API key (e.g., OpenRouter):
   brv providers connect openrouter --api-key YOUR_KEY

 * Switch Model:
   brv model switch <model-name>

 * Install Connectors:
   Connect ByteRover to your favorite coding tool:
   brv connectors install "Claude Code"

4. Workflows
Local vs. Cloud
| Feature | Local (Default) | Cloud (Optional) |
|---|---|---|
| Data Storage | On your machine | Synced to ByteRover servers |
| Privacy | 100% Private | Encrypted for collaboration |
| Teamwork | Manual sharing | Real-time team sync |
| Internet | Not required | Required for sync |
TUI vs. CLI
 * TUI: Interactive visual menu in the terminal. Best for configuration and browsing the context tree visually.
 * CLI: Command-based. Best for automation, headless mode, or quick commands like brv model switch.
> Clarity Note: Headless Mode > This refers to running the software without a graphical or interactive interface. This is useful for servers or automated scripts where a human isn't there to click buttons.
> 
5. FAQ & Troubleshooting
 * Do I need an account? No, you can use local models or external providers via API keys without an account. An account is only needed for the built-in LLM or cloud sync.
 * Where is the data stored? All context is stored in a hidden .brv folder within your project directory.
 * How does curation work? You can manually refine the context tree or let ByteRover's algorithms automatically pick the most relevant files for a specific coding task.

