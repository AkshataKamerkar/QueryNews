from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

class NewsCrew:
    """
    This class initializes and manages the AI-powered news summarization workflow.
    It organizes agents and tasks into a structured workflow using CrewAI.
    """

    def __init__(self, agents, tasks):
        """
        Initializes the NewsCrew with specified agents and tasks.
        
        :param agents: List of AI agents handling different tasks.
        :param tasks: List of tasks to be executed in sequence.
        """
        self.crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential  # Ensures tasks are executed in order
        )

    def get_crew(self):
        """
        Returns the initialized Crew instance.
        This method can be used to access the crew setup from other modules.
        """
        return self.crew

# Instantiate the NewsCrew with defined agents and tasks
news_crew = NewsCrew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task]
).get_crew()
