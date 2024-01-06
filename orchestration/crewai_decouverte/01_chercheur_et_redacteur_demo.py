import os
from crewai import Agent, Task, Crew, Process

# You can choose to use a local model through Ollama for example.
# In this case we will use OpenHermes 2.5 as an example.
#
from langchain.llms import Ollama
ollama_llm = Ollama(model="openhermes")

# If you are using an ollama like above you don't need to set OPENAI_API_KEY.
#os.environ["OPENAI_API_KEY"] = "Your Key"

# Define your tools, custom or not.
# Install duckduckgo-search for this example:
#
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals
researcher = Agent(
  role='Analyste de recherche principal',
  goal="Découvrez les développements de pointe en matière d'IA et de science des données",
  backstory="""Vous êtes analyste de recherche senior dans un groupe de réflexion technologique de premier plan.
  Votre expertise réside dans l'identification des tendances et technologies émergentes en matière d'IA et
  science des données. Vous avez le don de disséquer des données complexes et de les présenter
  des informations exploitables.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  # (optional) 
  llm=ollama_llm, #If you wanna use a local modal through Ollama, default is GPT4 with temperature=0.7

)
writer = Agent(
  role='Stratège de contenu technique',
  goal='Créez du contenu convaincant sur les avancées technologiques',
  backstory="""Vous êtes un stratège de contenu technologique renommé, connu pour votre perspicacité
  et des articles intéressants sur la technologie et l’innovation. Avec une profonde compréhension de
  Dans l’industrie technologique, vous transformez des concepts complexes en récits convaincants.""",
  verbose=True,
  # (optional) 
  llm=ollama_llm, #If you wanna use a local modal through Ollama, default is GPT4 with temperature=0.7
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Mener une analyse complète des dernières avancées en matière d’IA en 2024.
  Identifiez les tendances clés, les technologies révolutionnaires et les impacts potentiels sur l’industrie.
  Compilez vos résultats dans un rapport détaillé. Votre réponse finale DOIT être un rapport d'analyse complet""",
  agent=researcher
)

task2 = Task(
  description="""En utilisant les informations du rapport du chercheur, développez un article de blog engageant 
  qui met en évidence les avancées les plus significatives de l’IA.
  Votre message doit être informatif mais accessible, s'adressant à un public féru de technologie.
  Visez un récit qui capture l’essence de ces avancées et leurs
  implications pour l’avenir. Votre réponse finale DOIT être un billet de blog complet en français d'au moins 3 paragraphes.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  llm=ollama_llm, 
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)