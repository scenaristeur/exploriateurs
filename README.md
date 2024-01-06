# Les Exploriateurs

Une bande de joyeux pirates vous font partager leurs galères, leurs explorations dans le monde du numérique. 

# Les expéditions

- C'est quoi l'Intelligence artificielle générative ?
- llm un peu, llm beaucoup, llm passionnément, llm à la folie...
- génération d'images
- [A la découverte de CrewAi](orchestration/crewai_decouverte/README.md)

CrewAi est un orchestrateur d'agents (ou équipe de travailleurs) en intelligence artificielle accessible à tout le monde gratuitement en opensource sur un PC basic sans carte graphique spéciale (GPU). 
Nous allons ici installer un modèle de langage (ollama) en local. lancer un premier test avec deux agents en anglais, puis en français pour rédiger un article de blog sur les dernières évolutions en matière d'IA 

    - voici par exemple comment sont définis nos deux agents :

l'agent "effectuant les recherches" :
```
 role='Analyste de recherche principal',
  goal="Découvrez les développements de pointe en matière d'IA et de science des données",
  backstory="""Vous êtes analyste de recherche senior dans un groupe de réflexion technologique de premier plan.
  Votre expertise réside dans l'identification des tendances et technologies émergentes en matière d'IA et
  science des données. Vous avez le don de disséquer des données complexes et de les présenter
  des informations exploitables.""",
```

et l'agent "rédacteur de blog"

```
  role='Stratège de contenu technique',
  goal='Créez du contenu convaincant sur les avancées technologiques',
  backstory="""Vous êtes un stratège de contenu technologique renommé, connu pour votre perspicacité
  et des articles intéressants sur la technologie et l’innovation. Avec une profonde compréhension de
  Dans l’industrie technologique, vous transformez des concepts complexes en récits convaincants.""",

```




- Des ia décentralisées horde, petals, lilypad
