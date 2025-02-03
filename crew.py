from model.topic_content import Topicsummary
from crewai import Agent,Crew,Process,Task
from crewai.project import agent,crew,task,CrewBase
from langchain_ollama import OllamaLLM
import logging
from config import configure

log_file_save_path = configure.logging


logging.basicConfig(filename=log_file_save_path+'log_information.txt',level=logging.DEBUG,
                    format='%(asctime)s -%(levelname)s - %(name)s - %(message)s')


#variable declerations for logging
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')




@CrewBase
class TopicIdentifier():
    """ Topic idenification crew"""
    agents_config = 'config/agents.yaml'
    task_config = 'config/task.yaml'
    
    def __init__(self):
        self.llm = OllamaLLM(model="crewai-deepseek-r1",
                             api_key="NA")

    
    @agent
    def topic_identifier_agent(self) -> Agent:
        return Agent(config=self.agent_config['topic_identifier_agent'],
            allow_delegation= True,
            verbose=True,
            llm=self.llm)

    @agent
    def code_identifier_agent(self) -> Agent:
        return Agent(config= self.agents_config['code_identifier_agent'],
                     verbose=True,
                     llm=self.llm)
    
    @task
    def topic_coordination_task(self) ->Task:
        return Task(config = self.task_config['topic_coordination_task'],
                    agent=self.topic_identifier_agent,
                    )

    @task
    def code_analyzer_task(self) -> Task:
        return Task(config=self.task_config['code_analyzer_task'],
                    output_pydantic=Topicsummary)

    @crew
    def crew(self)-> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
