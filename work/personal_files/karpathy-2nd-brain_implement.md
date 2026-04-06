Here’s your content cleanly rendered as structured Markdown:


---

🧠 LLM Knowledge Base System

1. Core Philosophy: The "Simple & Flat" Rule

The primary goal is to avoid the "Notion Trap"—spending more time configuring tools than engaging with data.

No Databases → Use standard folders and text files (.md or .txt)

AI-Maintained → You are the collector; the AI is the librarian

Tool Agnostic → Works with VS Code, Cursor, Obsidian, Notepad, etc.



---

2. The Three-Folder Architecture

Organize your project directory into these three folders:

Folder	Purpose	Action

raw/	The "Junk Drawer"	Dump everything here. No organizing, no renaming.
wiki/	The "Organized Brain"	AI creates summaries, links topics, and maintains structure.
outputs/	The "Product"	Stores AI-generated reports, insights, and answers.



---

3. The "Schema" (CLAUDE.md)

This is the instruction manual for your AI.

Create a file named CLAUDE.md in your root directory:

# Knowledge Base Schema

## Wiki Rules

- Every topic gets its own `.md` file in `wiki/`
- Every file starts with a one-paragraph summary
- Use `[[topic-name]]` format for internal links
- Maintain an `INDEX.md` listing every topic with a one-line description
- Update existing wiki articles when new `raw/` sources are added


---

4. Automation & Collection

Manual Collection

Copy-paste notes, articles, or insights into markdown files in raw/


Automated Collection (Agent Browser)

Use tools like agent-browser to scrape content:

agent-browser open [URL]
agent-browser get text "article" > raw/article.md

AI Instruction

Tell your AI:

> "Scrape this URL and save the text to my raw folder."




---

5. Operation & Intelligence

🏗️ Compilation Step

Read everything in raw/.
Compile a wiki in wiki/ following CLAUDE.md rules.
Create INDEX.md first, then topic files.
Summarize and link everything.


---

🔍 Query Step

Use your wiki like a thinking partner:

"What are the contradictions between Source A and Source B?"

"What gaps exist in my understanding of [Topic]?"

"Summarize key insights across all notes on [Topic]"



---

🧪 Health Check (Monthly)

Prevent error compounding:

Ask AI to detect contradictions

Verify claims in wiki/ have sources in raw/

Identify weak or unsupported conclusions



---

6. Why This Works

📈 Compounding Intelligence

Every output you feed back improves future reasoning.

⚡ Zero Friction

No decision fatigue—just dump everything into raw/.

🔓 Future-Proof

Plain text = no vendor lock-in, ever.


---

🚀 Next Step

If you want, I can custom-design your CLAUDE.md based on:

Your trading system (Elder Impulse + ML)

Your AI research lab ideas

Your personal knowledge domains


That’s where this gets really powerful.