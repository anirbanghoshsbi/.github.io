Here’s a practical, no-nonsense System Guide you can drop into your repo as a .md file.
This is designed for fast setup + instant debugging, so you don’t get stuck in setup hell.


---

# ⚡ DeepTutor Quickstart + Debug Guide

---

# 🚀 1. 5-Minute Quickstart (Recommended Path)

## Step 1: Clone Repository
```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor


---

Step 2: Setup Environment

cp .env.example .env

Edit .env:

OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4
EMBEDDING_MODEL=text-embedding-3-large


---

Step 3: Start with Docker (Fastest Way)

docker-compose up -d


---

Step 4: Open Application

Frontend:

http://localhost:3000

Backend (API):

http://localhost:8000


---

Step 5: First Action (IMPORTANT)

1. Go to Knowledge Base


2. Upload a PDF / Markdown file


3. Wait for processing


4. Ask a question



👉 If you skip this → system will feel “broken”


---

🧠 2. Mental Model (Before You Use)

DeepTutor is NOT a chatbot.

It works like:

Knowledge Base → Agents → Tools → Answer

If something fails:

Either knowledge is missing

Or tool/agent failed



---

⚙️ 3. Core Components Checklist

Before debugging, check:

Component	Must Work

API Key	✅
LLM Model	✅
Embedding Model	✅
Backend Running	✅
Frontend Running	✅
Knowledge Base Created	✅



---

🐞 4. Quick Debug Checklist (90% Issues)

❌ Issue: “Nothing works / blank responses”

✅ Check:

API key added?

Model name correct?

Backend logs for errors



---

❌ Issue: “No answer from documents”

✅ Check:

Did you upload documents?

Did indexing complete?

Is correct knowledge base selected?



---

❌ Issue: “Model not responding”

✅ Check:

API quota exhausted?

Wrong model name?

Network issue?



---

❌ Issue: “Docker not working”

✅ Fix:

docker-compose down
docker-compose up --build


---

❌ Issue: “Frontend loads but backend fails”

✅ Check:

curl http://localhost:8000

If fails:

Backend is not running

Port conflict



---

🔍 5. Log-Based Debugging (MOST IMPORTANT)

Check Backend Logs:

docker logs -f deeptutor-backend


---

Look for:

Error Type	Meaning

Authentication Error	API key issue
Rate Limit	Too many requests
Model Not Found	Wrong model name
Timeout	Network / API slow



---

🧪 6. Minimal Test Workflow (Sanity Check)

Run this to verify system:


---

Test 1: Basic LLM

Ask:

What is 2+2?

👉 If fails → LLM config broken


---

Test 2: Knowledge Retrieval

1. Upload small PDF


2. Ask:



Summarize this document

👉 If fails → RAG/indexing issue


---

Test 3: Solve Mode

Ask:

Solve: x^2 + 5x + 6 = 0

👉 If fails → agent/tool issue


---

🧰 7. Common Fix Patterns

🔧 Fix 1: Reset Everything

docker-compose down -v
docker-compose up --build


---

🔧 Fix 2: Rebuild Knowledge Base

Delete KB

Re-upload files



---

🔧 Fix 3: Simplify Config

Use:

MODEL_NAME=gpt-3.5-turbo

👉 Helps isolate issues


---

⚡ 8. Performance Tips

Faster Responses:

Use smaller models

Reduce document size

Limit query complexity



---

Better Accuracy:

Use high-quality PDFs

Avoid noisy documents

Structure content



---

🧠 9. How to Use Efficiently (Power User Flow)

Daily Workflow:

1. Upload content


2. Ask questions


3. Generate quizzes


4. Solve problems


5. Save outputs




---

Golden Rule:

Garbage In → Garbage Out

👉 Quality of knowledge base = quality of system


---

🔌 10. Advanced Debug (If You're Stuck)

Step 1: Check API manually

curl https://api.openai.com/v1/models


---

Step 2: Run backend manually

cd src
python main.py


---

Step 3: Check frontend logs

cd web
npm run dev


---

🚨 11. Most Common Beginner Mistakes

❌ Forgetting API keys

❌ Not uploading documents

❌ Expecting ChatGPT-like behavior

❌ Ignoring logs

❌ Using wrong model names



---

🎯 12. Quick Success Recipe

If you just want it working:

1. Use Docker


2. Add OpenAI API key


3. Upload 1 clean PDF


4. Ask simple questions



👉 Done. System works.


---

🧠 13. Final Insight

DeepTutor works best when:

You treat it as a learning system

Not a chat interface



---

⚡ TL;DR

If broken:

Check API → Check Logs → Check Knowledge Base


---

🚀 You’re Ready

Once this works:

Start experimenting with:

Agents

Tools

Knowledge graphs



👉 That’s where the real power begins.

---

If you want, I can take this one step further for you:

👉 Build a **“DeepTutor Debug Dashboard mindset”**  
(where each failure maps to agent/tool/memory layer—super useful for your AI lab vision)

or  

👉 Create a **minimal DeepTutor clone architecture using Gemma (E4B)** for your local experiments

Just tell me 👍