# Wiki: Local Claude Code & Gemma 4 Integration
This guide provides a comprehensive walkthrough for running **Claude Code** locally using **Gemma 4** via **Ollama**. This setup is completely free, requires no API keys or subscriptions, and ensures full privacy by keeping all data on your machine.
## 1. Overview & Prerequisites
This setup allows you to leverage Google’s Gemma models within the Claude Code interface by redirecting cloud requests to a local server.
### System Requirements
 * **Editor:** Visual Studio Code (VS Code) installed.
 * **Environment:** Node.js (Version 18 or higher).
 * **Connectivity:** Stable internet connection for the initial model download (7GB–18GB).
## 2. Step-by-Step Installation
### Step 1: Install Ollama (The Engine)
Ollama acts as the local server for your AI models.
 * **macOS:** Download from ollama.com/download and install like a standard application.
 * **Windows:** Download and run the installer from ollama.com/download.
 * **Linux:** Run the following command in your terminal:
   curl -fsSL ollama.com/install.sh | sh
 * **Verification:** Run ollama --version in your terminal to confirm success.
### Step 2: Download Gemma 4
Choose the model version based on your system's hardware (RAM):
| Hardware Tier | RAM | Command |
|---|---|---|
| **Low-end** | 8GB | ollama pull gemma4:e2b |
| **Recommended** | 16GB | ollama pull gemma4:e4b |
| **High-end** | 32GB | ollama pull gemma4:26b |
 * **Note:** Download size ranges from 7GB to 18GB.
 * **Verification:** Run ollama list to see your downloaded models.
### Step 3: Install Claude Code Extension
 1. Open **VS Code**.
 2. Press Ctrl + Shift + X to open the Extensions marketplace.
 3. Search for **Claude Code** (published by Anthropic) and install it.
 4. Once installed, a **Lightning Bolt (⚡)** icon will appear in the sidebar.
### Step 4: Configure Local Redirection
To stop Claude from trying to reach the cloud, you must edit your VS Code settings.
 1. Press Ctrl + Shift + P.
 2. Search for and select: **Preferences: Open User Settings (JSON)**.
 3. Paste the following block inside the JSON braces:
```json
"claude-code.env": {
  "ANTHROPIC_BASE_URL": "http://localhost:11434",
  "ANTHROPIC_API_KEY": "",
  "ANTHROPIC_AUTH_TOKEN": "ollama"
}

```
## 3. Running the System
 1. **Initialize Ollama:** Open your terminal and run:
   ollama serve
   *(Keep this terminal window open/running).*
 2. **Activate Claude Code:** In VS Code, click the **⚡ icon** in the sidebar.
 3. **Select Model:** When prompted for a model, type the exact name you downloaded (e.g., gemma4:e4b).
### Common Tasks to Try:
 * *"Explain this file"*
 * *"Write a function"*
 * *"Refactor this code"*
## 4. Troubleshooting & Quick Fixes
| Issue | Cause | Solution |
|---|---|---|
| **"Unable to connect"** | Ollama is not running. | Run ollama serve in your terminal. |
| **Asked to sign in** | JSON config error. | Re-check settings.json for syntax errors (commas/brackets). |
| **Very slow responses** | Model too heavy for RAM. | Switch to a smaller model (e.g., gemma4:e2b). |
| **Model not found** | Typo in model name. | Run ollama list and copy the name exactly. |
*Follow for more AI contents like this!*
