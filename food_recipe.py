from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from agno.embedder.ollama import OllamaEmbedder
load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile")
embedder = OllamaEmbedder(id="mxbai-embed-large", dimensions=1024)
vector_db = LanceDb(
    table_name="recipe1",
    uri="/tmp/lancedb",
    search_type=SearchType.hybrid,
    embedder=embedder
)
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://www.fssai.gov.in/upload/knowledge_hub/9582262a819e8764cdBook_Tadke_bina_Zaika_14_06_2022.pdf"],
    vector_db=vector_db
)
knowledge_base.load(upsert=True)
from agno.agent import Agent

agent = Agent(
    model=llm,
    # Enable RAG
    knowledge=knowledge_base,
    add_context=True,
    # Add references to the original documents
    add_references=True,
    description="You are a Indian cuisine expert!",
    instructions=[
        "Search your knowledge base for Indian recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    search_knowledge=False,
    add_history_to_messages=True,
    num_history_responses=10,
    markdown=True,
    # debug_mode=True,

)

prompt = "How do I make Mutton Yakni Biryani"
response = agent.run(prompt)
print(response.content)

