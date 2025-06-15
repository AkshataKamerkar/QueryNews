
# AI-Powered News Summarizer

This project is an AI-powered news summarizer using FastAPI for the backend and Streamlit for the frontend. It uses CrewAI and Groq API to gather, summarize, and present news articles in a concise and user-friendly way.


## Features

* **AI-Powered Summaries:** Fetch news and generate short, concise summaries using advanced AI models.
* **Streamlit Frontend:** Beautiful and user-friendly UI for users to input their queries and view results.
* **FastAPI Backend:** Efficient API to handle requests from the frontend and process data using CrewAI agents.
## Requirements

* Any Python IDE
* Python 3.8 or higher
* pip for installing dependencies
## Installation

**STEP 1:** Clone the repository

### Backend (FastAPI)

**STEP 2:** Install Dependencies
* Make sure you are in the backend folder, then install the necessary dependencies.

```
cd backend
pip install -r requirements.txt
```

**STEP 3:** Setup Environment Variables 
* Create a .env file in the backend folder to store your API keys and provider settings.

```
GROQ_API_KEY=your_groq_api_key_here
LITELLM_PROVIDER=groq
```

**STEP 4:** Run the FastAPI Application
* After installing the dependencies and setting up the environment, you can run the FastAPI server with:

```
uvicorn --reload app:app
```
This will start the FastAPI backend at http://127.0.0.1:8000/.

#### **Test the Endpoint:**

Navigate to http://127.0.0.1:8000/docs in your browser. This will open FastAPI's interactive API documentation, where you can:

* Test the `/summarize_news` endpoint by clicking on it.
* Input the necessary parameters, such as topic and date.
* Press the "Execute" button to test and view the response directly.

You can use the interface to send requests to the backend without needing an external tool like Postman.

### Frontend (Streamlit)
* Make sure you are in the frontend folder.
```
cd frontend 
```

**STEP 5:** Run the Streamlit Application 

```
streamlit run app.py
```
This will open the Streamlit UI in your browser. You can enter a topic and date to get a summarized news report.

## API Docs


Once the FastAPI backend is running, visit http://127.0.0.1:8000/docs to see the automatic Swagger documentation for the available API endpoints.

https://github.com/user-attachments/assets/3d2e4111-37fe-4cf6-8509-469d77491762


* **POST /summarize_news -**
Accepts topic (string) and date (string, in the format YYYY-MM-DD), and returns a summarized news article.

**Request Body Example:**
```
{
  "topic": "RAG",
  "date": "2024-07-06"
}
```

**Response Example:**
```
{
  "summary": {
    "raw": "**\n\n**RAG Technology Sees Significant Advancements in 2024**\n\nIn a rapidly evolving technological landscape, RAG (Retrieval-Augmented Generation) continues to make waves with groundbreaking developments. Here are the top three news highlights for July 6, 2024:\n\n1. **Faster Data Retrieval with RAG Technology**  \n   The latest advancements in RAG technology have significantly improved data retrieval speeds. This enhancement ensures that users can access information more efficiently, making it a valuable tool for both professionals and researchers alike.\n\n2. **New RAG Tools Boost Accuracy**  \n   Innovators have introduced new RAG tools designed to enhance the accuracy of information extraction. These tools are set to revolutionize industries that rely heavily on precise data, such as healthcare and finance.\n\n3. **RAG and AI Integration for Smarter Decisions**  \n   The integration of RAG with artificial intelligence has taken decision-making processes to the next level. By leveraging AI's analytical capabilities, RAG now offers more informed and data-driven insights, aiding businesses in making smarter strategic decisions.\n\nThese developments underscore RAG's pivotal role in shaping the future of data management and analysis, promising even more exciting innovations in the years to come.",
    "pydantic": null,
    "json_dict": null,
    "tasks_output": [
      {
        "description": "Conduct research and find latest news articles about RAG for 2024-07-06. Provide a **short, to-the-point summary** (under 3 sentences). KEEP IT UNDER 50 WORDS. KEEP IT PRECISE. GIVE TOP 3 NEWS.",
        "name": null,
        "expected_output": "A list of summarized key news articles related to RAG on 2024-07-06. Provide a **short, to-the-point summary** (under 3 sentences). KEEP IT UNDER 50 WORDS. KEEP IT PRECISE. GIVE TOP 3 NEWS.",
        "summary": "Conduct research and find latest news articles about RAG for...",
        "raw": "1. RAG technology advancements in 2024 enable faster data retrieval. 2. New RAG tools improve accuracy in information extraction. 3. RAG integration with AI enhances decision-making processes.\n```",
        "pydantic": null,
        "json_dict": null,
        "agent": "Senior Researcher",
        "output_format": "raw"
      },
      {
        "description": "Summarize and write a news article about RAG for 2024-07-06 using the research findings. GIVE TOP 3 NEWS, KEEP IT PRECISE.",
        "name": null,
        "expected_output": "A well-structured, concise summary of news articles related to RAG on 2024-07-06. GIVE TOP 3 NEWS, KEEP IT PRECISE.",
        "summary": "Summarize and write a news article about RAG for 2024-07-06...",
        "raw": "**\n\n**RAG Technology Sees Significant Advancements in 2024**\n\nIn a rapidly evolving technological landscape, RAG (Retrieval-Augmented Generation) continues to make waves with groundbreaking developments. Here are the top three news highlights for July 6, 2024:\n\n1. **Faster Data Retrieval with RAG Technology**  \n   The latest advancements in RAG technology have significantly improved data retrieval speeds. This enhancement ensures that users can access information more efficiently, making it a valuable tool for both professionals and researchers alike.\n\n2. **New RAG Tools Boost Accuracy**  \n   Innovators have introduced new RAG tools designed to enhance the accuracy of information extraction. These tools are set to revolutionize industries that rely heavily on precise data, such as healthcare and finance.\n\n3. **RAG and AI Integration for Smarter Decisions**  \n   The integration of RAG with artificial intelligence has taken decision-making processes to the next level. By leveraging AI's analytical capabilities, RAG now offers more informed and data-driven insights, aiding businesses in making smarter strategic decisions.\n\nThese developments underscore RAG's pivotal role in shaping the future of data management and analysis, promising even more exciting innovations in the years to come.",
        "pydantic": null,
        "json_dict": null,
        "agent": "Writer",
        "output_format": "raw"
      }
    ],
    "token_usage": {
      "total_tokens": 16692,
      "prompt_tokens": 10349,
      "cached_prompt_tokens": 0,
      "completion_tokens": 6343,
      "successful_requests": 17
    }
  }
}
```

## Known Errors -

### **Maximum Rate Limit Error**

**Error Message:**

```
ERROR:root:LiteLLM call failed: litellm.RateLimitError: RateLimitError: GroqException - {"error":{"message":"Rate limit reached for model `deepseek-r1-distill-llama-70b` in organization `org_01j679k5xxek99npd0zvhwzs56` service tier `on_demand` on tokens per minute (TPM): Limit 6000, Used 5750, Requested 2609. Please try again in 23.587s. Visit https://console.groq.com/docs/rate-limits for more information.","type":"tokens","code":"rate_limit_exceeded"}}
```

**Description:**

* This error occurs when the rate limit for the Groq model (deepseek-r1-distill-llama-70b) is reached. The model's token-per-minute (TPM) limit has been exceeded due to frequent requests.

**Current Solution:**

* Refresh the page and try again after a while.
* You may also consider using another LLM with a higher context limit or upgrading your service tier for higher limits.

## Demo 
* To see the application in action, check out the following demo video:

  
https://github.com/user-attachments/assets/799ebbe3-cc68-4eca-9fb1-3f04e8d17639

