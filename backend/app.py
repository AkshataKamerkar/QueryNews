from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew import news_crew  # Importing the Crew instance from crew.py
from dotenv import load_dotenv
import time
from litellm import RateLimitError

# Load environment variables
load_dotenv()

class NewsRequest(BaseModel):
    """
    Pydantic model to validate incoming request data.
    Expects a 'topic' and 'date' (YYYY-MM-DD format).
    """
    topic: str
    date: str

class NewsSummarizerAPI:
    """
    This class initializes and manages the FastAPI-based News Summarizer API.
    It defines endpoints for processing news summaries using CrewAI.
    """

    def __init__(self):
        """
        Initializes the FastAPI application instance.
        """
        self.app = FastAPI()

        # Define API routes
        self.app.post("/summarize_news")(self.summarize_news)
        self.app.get("/")(self.root)

    async def summarize_news(self, request: NewsRequest):
        """
        Endpoint to generate a summarized news report using CrewAI.
        
        :param request: JSON request containing 'topic' and 'date'.
        :return: JSON response with summarized news.
        """
        try:
            # Running the CrewAI workflow with provided inputs
            result = news_crew.kickoff(inputs={"topic": request.topic, "date": request.date})
            return {"summary": result}
        except RateLimitError:
            raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again later.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

    def root(self):
        """
        Default endpoint to verify API status.
        """
        return {"message": "Welcome to the CrewAI News Summarizer API! Use /summarize_news to get a news summary."}

# Instantiate API
news_api = NewsSummarizerAPI()

# FastAPI app instance
app = news_api.app
