
# ByteRover: The Complete Wiki & Quickstart Guide

## 1. Overview
ByteRover is a **local-first AI context engineering** platform for coding agents. It provides agents (like Cursor, Claude Code, or Windsurf) with a "persistent memory" of your project by storing knowledge locally.

* **Local-First:** Your data stays on your machine by default.
* **Context Engineering:** Structuring project data so AI models can provide more accurate, relevant answers.
* **BYOK (Bring Your Own Key):** Use your own API keys from providers like OpenAI or Anthropic without needing a ByteRover account.

---

## 2. Installation
Choose the method that fits your environment.

### **macOS (Apple Silicon) & Linux**
```bash
curl -fsSL [https://byterover.dev/install.sh](https://byterover.dev/install.sh) | sh

> Note: If brv isn't found after installation, run: export PATH="$HOME/.brv-cli/bin:$PATH"
> 
Windows & All Platforms (via NPM)
Requires Node.js 20+
npm install -g byterover-cli

Verify Installation
brv --version

3. Initial Setup & Launch
Navigate to your project directory. Running ByteRover for the first time creates a .brv/ folder to store your context tree.
Launch the TUI (Interactive)
The Terminal User Interface (TUI) allows you to manage everything visually.
cd path/to/your/project
brv

4. LLM Providers & Models
ByteRover acts as a bridge to your preferred AI model.
Connecting Providers
| Provider | CLI Command |
|---|---|
| OpenRouter | brv providers connect openrouter --api-key YOUR_KEY |
| OpenAI (OAuth) | brv providers connect openai --oauth |
| Anthropic | brv providers connect anthropic --api-key YOUR_KEY |
| Built-in LLM | brv login (then follow prompts) |
Managing Models
 * Switch Model: brv model switch <model-name>
 * Switch Provider: brv providers switch <provider-id>
 * List Providers: (Inside TUI) type /providers
5. Agent Connectors
Connectors allow your AI IDEs and CLI tools to access ByteRover's context.
Installation
# General installation
brv connectors install "Claude Code"

# Install as a specific type (e.g., MCP for Cline/Zed)
brv connectors install "Cline" --type mcp

Connector Types
 * Skill: Default for most agents (Cursor, Windsurf, GitHub Copilot).
 * MCP: Standard for Augment, Cline, and Zed.
 * Hook: Specifically for Claude Code lifecycle.
 * Rules: For agents using .cursorrules or similar configuration files.
6. Curating Context (Adding Knowledge)
Curation "teaches" ByteRover which parts of your codebase are important.
Manual Curation
 * CLI: brv curate "Explain the project architecture and database schema"
 * TUI: Type /curate <description>
Agent-Led Curation
Ask your AI agent (Cursor/Claude) directly in their chat window:
> "Use the brv curate command to index the authentication flow in this project."
> 
7. Querying Context (Retrieving Knowledge)
Once curated, you can pull that specific context back into your conversation.
Manual Query
 * CLI: brv query "How does the unit testing strategy work here?"
 * TUI: Type /query <question>
Agent-Led Query
Ask your coding agent:
> "Use brv query to find the documentation for our API error handling."
> 
8. Maintenance & Status
 * Check Context Tree: brv status
   Shows the organized domains inside .brv/context-tree.
 * Daemon-First Architecture: ByteRover runs a background "daemon" that auto-starts on any command. It ensures your terminal and IDE settings stay synchronized.
FAQ & Clarity Notes
 * Daemon: A background process that ensures your terminal settings and your AI IDE stay in sync.
 * Headless Mode: Running ByteRover without an interface, useful for automated scripts or servers.
 * Account Requirements: An account is only needed for cloud syncing or using the "ByteRover Built-in" free LLM tier.

***

### **How to save this:**
1.  **Copy** the entire content inside the block above.
2.  **Create a new file** on your computer.
3.  **Name it** something like `ByteRover_Wiki.md`.
4.  **Paste** the content and save.

