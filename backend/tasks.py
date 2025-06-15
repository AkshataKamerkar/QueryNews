from crewai import Task
from agents import news_researcher, news_writer

class NewsTaskFactory:
    """
    Factory class responsible for creating research and writing tasks.
    Ensures tasks are well-defined with the correct agents and expected outputs.
    """
    
    def __init__(self, researcher, writer):
        self.researcher = researcher
        self.writer = writer

    def create_research_task(self):
        """Creates and returns the news research task."""
        return Task(
            description="Conduct research and find latest news articles about {topic} for {date}. "
                        "Provide a **short, to-the-point summary** (under 3 sentences). "
                        "KEEP IT UNDER 50 WORDS. KEEP IT PRECISE. GIVE TOP 3 NEWS.",
            agent=self.researcher,
            expected_output="A list of summarized key news articles related to {topic} on {date}. "
                            "Provide a **short, to-the-point summary** (under 3 sentences). "
                            "KEEP IT UNDER 50 WORDS. KEEP IT PRECISE. GIVE TOP 3 NEWS."
        )

    def create_write_task(self):
        """Creates and returns the news writing task."""
        return Task(
            description="Summarize and write a news article about {topic} for {date} using the research findings. "
                        "GIVE TOP 3 NEWS, KEEP IT PRECISE.",
            agent=self.writer,
            expected_output="A well-structured, concise summary of news articles related to {topic} on {date}. "
                            "GIVE TOP 3 NEWS, KEEP IT PRECISE."
        )

# Create tasks using the factory class
task_factory = NewsTaskFactory(news_researcher, news_writer)
research_task = task_factory.create_research_task()
write_task = task_factory.create_write_task()
