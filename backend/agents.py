from crewai import Agent
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

class LLMInitializer:
    """
    Class to handle the initialization of the Language Model (LLM).
    Ensures the API key is loaded properly and creates a ChatGroq instance.
    """
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Missing GROQ_API_KEY. Please set it in your environment variables.")
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        """Creates and returns an instance of ChatGroq with predefined parameters."""
        return ChatGroq(
            model="groq/deepseek-r1-distill-llama-70b",
            verbose=True,
            temperature=0.5,
            api_key=self.api_key,
            max_token=50
        )

class NewsAgentFactory:
    """
    Factory class responsible for creating AI agents for news research and writing.
    """
    def __init__(self, llm):
        self.llm = llm

    def create_researcher(self):
        """Creates and returns a news researcher agent."""
        return Agent(
            role="Senior Researcher",
            goal="Uncover latest news and breakthroughs in {topic} for {date}. "
                 "Provide a **short, to-the-point summary** (under 3 sentences). "
                 "KEEP IT UNDER 50 WORDS, KEEP IT PRECISE. GIVE TOP 3 NEWS.",
            verbose=True,
            backstory="An expert journalist, always on the lookout for the most relevant news in any given field.",
            llm=self.llm,
            memory=False,
            allow_delegation=True,
            max_iter=1
        )

    def create_writer(self):
        """Creates and returns a news writer agent."""
        return Agent(
            role="Writer",
            goal="Summarize news and write a compelling article about {topic} for {date}. "
                 "GIVE TOP 3 NEWS, KEEP IT PRECISE.",
            verbose=True,
            memory=False,
            backstory="An expert writer who crafts concise and engaging news summaries.",
            llm=self.llm,
            allow_delegation=False,
            max_iter=1
        )

# Initialize LLM
llm_initializer = LLMInitializer()

# Create agents using the factory class
agent_factory = NewsAgentFactory(llm_initializer.llm)
news_researcher = agent_factory.create_researcher()
news_writer = agent_factory.create_writer()
