import os
from crewai import Agent, Task, Crew, Process
from langchain.agents import AgentType, initialize_agent, load_tools
#from langchain.llms import OpenAI

#os.environ["OPENAI_API_KEY"] = "Your Key"

from langchain.llms import Ollama
#ollama_openhermes = Ollama(model="mistral")
ollama_openhermes = Ollama(model="openhermes")

# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

dm = Agent(
  role='Dungeon Master',
  goal='Host a short Dungeons and Dragons Session to do with raider goblins stealing the village food.',
  backstory="You're a world class Dungeon Master.",
#  tools=[
#    SearchTools.search_internet,
#    BrowserTools.scrape_and_summarize_website,
#  ],
  llm=ollama_openhermes, # Ollama model passed here
  verbose=True,
  allow_delegation=False
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)

ranger = Agent(
  role='ranger',
  goal='Role play your character. Be brave and lead the party to complete the quest.',
  backstory="You're a famous Level 3 Human Ranger, specialized on Hunting, Tracking, and Bowmanship.",
  llm=ollama_openhermes, # Ollama model passed here
  verbose=True,
  allow_delegation=False
)

fighter = Agent(
  role='fighter',
  goal='Role play your character and assist the party in completing the objective.',
  backstory="You're a newly recruited Level 1 Human Fighter with a shortsword.",
  llm=ollama_openhermes, # Ollama model passed here
  verbose=True,
  allow_delegation=False
)


# Create tasks for your agents
task1 = Task(description='Create a short Quest.', agent=dm)
task2 = Task(description='Explain the beginning scene of the quest. Only give details as the players unveil them.', agent=dm)

task3 = Task(description='Choose your action and the direction for the party.', agent=ranger)
task4 = Task(description='Choose your action and what you would like to do.', agent=fighter)
task5 = Task(description='Continue the quest accordingly making it unique and interesting.', agent=dm)
task6 = Task(description='If the players have successfully completed the quest, write "YOU WON".', agent=dm)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[dm, ranger, fighter],
  tasks=[task1, task2, task3, task4, task5, task6],
  verbose=2, #True, # Crew verbose more will let you know what tasks are being worked on
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()
crew.tasks.remove(task1)
crew.tasks.remove(task2)
while "YOU WON" not in result:
  result = crew.kickoff()