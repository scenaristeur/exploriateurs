# utilisation de CREWAI
```
environnement : Linux Mint
```


Je suis tombé sur cette vidéo https://www.youtube.com/watch?v=GKr5URJvNDQ
- autres vidéos sur le sujet https://www.youtube.com/watch?v=tnejrr-0a94
- dépôt https://github.com/joaomdmoura/crewAI
- site officiel : https://www.crewai.io/
- doc : https://github.com/joaomdmoura/CrewAI/wiki


CrewAi est un orchestrateur, comme [autogen de Microsoft](https://microsoft.github.io/autogen/). 
Le but d'un orchestrateur et d'organiser une équipe d'agents, de leur assigner des tâches, de vérifier qu'elles sont bien exécutées.

Comme toujours, pour limiter les coûts d'utilisation de l'API chez OpenAi, on va préférer utiliser un modèle de langage local et Opensource, et ça tombe bien,
[CrewAi est compatible avec ollama](https://github.com/joaomdmoura/crewAI#local-open-source-models). 
Sans plus tarder, lançons les investigations.

# installation Ollama
- https://ollama.ai/download
- sur linux debian, il suffit de lancer la commande `curl https://ollama.ai/install.sh | sh`
- installation et test du model `ollama run openhermes`

![installation ollama openhermes](images/install_ollama_openhermes.png)




# test de crewAI
- evidemment, on peut isoler le process dans un environnement virtuel (conda, venv)[lien pourquoi un environnement python virtuel ?]

- installation de crewAi avec la commande `pip install crewai -U`
L'exemple que l'on va tester utilise le moteur de recherche DuckDuckGo, donc nous devons également installer ce package python avec la commande `pip install duckduckgo-search -U`


# Création de notre première Crew, ou équipe. 
- nous allons reprendre l'exemple https://github.com/joaomdmoura/crewAI#getting-started
et le modifier pour qu'il utilise ollama -> [01_research_and_writer_demo.py](<01_research_and_writer_demo.py>)

# lancement de la crew
```$ python 01_research_and_writer_demo.py ```

![Alt text](images/01_lancement_crew.png)


![Alt text](images/01_duckduck.png)


![Alt text](images/01_resultat.png)

Une fois les résultats récupérés, le processus de rédaction de l'article commence

![Alt text](images/01_resultat_bis.png)

![Alt text](images/01_reflexion.png)

![Alt text](images/01_blog_post.png)


# si on veut monter une équipe d'experts français ? 
Rien de plus simple, en utilisant https://translate.google.fr/?hl=fr  on peut traduire les différents prompts, et instructions données aux agents -> [01_chercheur_et_redacteur_demo.py](01_chercheur_et_redacteur_demo.py)




