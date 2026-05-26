# Agentic RAG – Indian Recipe AI Chef (Agno + Groq + Ollama + LanceDB)
I built an Agentic RAG pipeline that can generate a complete Indian recipe step by step, acting like an AI chef that both retrieves and reasons over culinary knowledge.

How it works
📄 Recipe-first retrieval with LanceDB
Recipes are indexed from an Indian recipe PDF into LanceDB using an Ollama-based embedding model (mxbai-embed-large), enabling hybrid semantic search over the document.

🌐 Web fallback with DuckDuckGo
If the requested dish is not well-covered in the PDF, the agent intelligently switches to DuckDuckGo tools for live web search, filling knowledge gaps while still preferring curated sources.

🧠 Agentic RAG with Agno
The core logic is orchestrated via Agno, which wires together the knowledge base, web tools, and LLM into a single agent that can search, decide when to use tools, and respond with structured cooking instructions.

⚡ Low-latency reasoning with Groq
The main LLM is served via Groq (llama-3.3-70b-versatile), providing fast, low-latency inference so users can iterate on recipe ideas in real time.

🧩 Local embeddings with Ollama
Ollama powers the embedding pipeline, generating dense vector representations for recipes that are stored and searched via LanceDB.

🎨 Interactive UI with Streamlit
A Streamlit front end turns the pipeline into an interactive demo where users can type any Indian dish (e.g., Mutton Yakhni Biryani) and get a step‑by‑step, well-formatted recipe response.

Features
🔍 RAG-native design: Agent is initialized with add_context=True and a PDFUrlKnowledgeBase, so retrieval is baked into the reasoning loop.

🧭 Tool-aware behavior: Custom instructions guide the agent to prefer the PDF knowledge base and only fall back to web search when necessary.

📚 Citable outputs: Responses can include references back to the original PDF, making steps explainable and auditable.

💬 Conversation-aware: History is preserved across turns (add_history_to_messages=True), allowing follow-up questions like “Can you make it spicier?” or “Suggest a vegetarian alternative.”

Tech stack
Framework: Agno (Agentic RAG & tool orchestration)

LLM Runtime: Groq (LLM inference for llama-3.3-70b-versatile)

Embeddings: Ollama + mxbai-embed-large

Vector DB: LanceDB with hybrid search

Knowledge Source: Indian recipe PDF (FSSAI “Tadke Bina Zaika” cookbook)

Web Search Tool: DuckDuckGoTools (for live recipe enrichment)

UI: Streamlit app for interactive recipe exploration

Example query
“How do I make Mutton Yakhni Biryani?”

The agent first checks the PDF-based LanceDB knowledge base for relevant sections; if coverage is low, it augments context with DuckDuckGo search and then returns a clear, step‑by‑step Indian recipe with ingredients, preparation, and cooking instructions.
