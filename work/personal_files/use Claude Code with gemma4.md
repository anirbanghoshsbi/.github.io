
To ensure I haven't left out a single detail from the material provided, I have synthesized everything—from your personal asset inventory to the technical guide—into this master **Knowledge Base Wiki**.
I have added the specific nuances (like the "no terminal" requirement for Mac and the "15-minute setup" timeframe) that were missing from the previous iteration.
# 🗂️ Master Knowledge Base Wiki

## 1. Guide: Claude Code with Gemma 4 (Beginner's Guide)
*How to run Claude Code completely free with no subscriptions and no API keys.*
**Value Proposition:**
 * **Cost:** Completely free; no API costs.
 * **Setup Time:** 15 minutes.
 * **Privacy:** Full privacy; nothing leaves your device.
 * **Hardware:** Works on just your laptop.
### 📋 Prerequisites
 * **VS Code** installed.
 * **Node.js** (version 18+).
 * **Stable Internet** (required for the one-time model download).
### 🛠️ Step 1: Install Ollama (The Engine)
Ollama runs AI models locally on your machine.
 * **Mac:** Download at ollama.com/download. Install like a normal app; **no terminal needed**.
 * **Windows:** Download and install from ollama.com/download.
 * **Linux:** Run curl -fsSL ollama.com/install.sh | sh.
 * **Verify:** Run ollama --version to check.
### 📥 Step 2: Download Gemma 4
Select the model based on your system RAM. Note: These are big downloads (7GB–18GB), so **give it time**.
 * **Low-end (8GB RAM):** ollama pull gemma4:e2b
 * **Recommended (16GB RAM):** ollama pull gemma4:e4b
 * **High-end (32GB RAM):** ollama pull gemma4:26b
 * **Verify:** Command ollama list.
### 🔌 Step 3: Install Claude Code in VS Code
 1. Open VS Code.
 2. Press Ctrl + Shift + X.
 3. Search for **Claude Code** (the one by Anthropic).
 4. After installation, a **⚡ icon** will appear in the sidebar.
### ⚙️ Step 4: Connect Claude Code to Ollama
This redirects Claude from the cloud to your local server.
 1. Press Ctrl + Shift + P.
 2. Search: **open user settings (json)**.
 3. Paste this inside the configuration:
```json
"claude-code.env": {
  "ANTHROPIC_BASE_URL": "http://localhost:11434",
  "ANTHROPIC_API_KEY": "",
  "ANTHROPIC_AUTH_TOKEN": "ollama"
}

```
**Effect:** It routes everything to your local Ollama server; nothing leaves your device.
### 🚀 Step 5: Run Everything
 1. **Start Server:** Run ollama serve and leave it running.
 2. **Open Extension:** Click the **⚡ icon** in VS Code.
 3. **Model Selection:** Type gemma4:e4b (or your chosen model).
**Commands to try:**
 * *"Explain this file"*
 * *"Write a function"*
 * *"Refactor this code"*
### 💡 Troubleshooting (Quick Fixes)
| Issue | Potential Cause | Fix |
|---|---|---|
| **"Unable to connect"** | Server not active | Run ollama serve. |
| **Asked to sign in** | JSON Config error | Check for missing commas/brackets in settings. |
| **Very slow responses** | Model too big | Switch to gemma4:e2b. |
| **Model not found** | Name mismatch | Run ollama list and copy the exact name. |
### 📝 Quick Recap
You have built a **free Claude setup** powered by **local AI** with **no API costs**.
*Follow for more AI contents like this!!!*
