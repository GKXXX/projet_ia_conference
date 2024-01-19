# Projet IA Veille Technologique

Ce projet en Python a pour objectif de récupérer des articles via un flux RSS et, à l'aide d'un modèle de Langage de Modélisation (LLM) en intelligence artificielle, de générer un résumé pour chaque article.

## Configuration

1. Vérifiez que Python 3 et pip sont installés en exécutant les commandes suivantes :

   ```bash
    python --version
   ```

   ```bash
    pip --version
   ```

2. Créez un environnement virtuel (si vous le souhaitez) et activez-le en vous assurant d'être dans le dossier du projet :

   ```bash
   python -m venv venv
   ```

   ou

   ```bash
   python3 -m venv venv
   ```

   ***

   ```bash
   source venv/bin/activate[Ollama](https://ollama.ai/)
   ```

3. Assurez-vous également d'avoir installé le modèle openchat avec [Ollama](https://ollama.ai/) :

   ```bash
   ollama pull openchat
   ```

4. Installez les dépendances nécessaires :

   ```bash
   pip install -r requirements.txt
   ```

   ou

   ```bash
   pip3 install -r requirements.txt
   ```

5. Exécutez le script main.py :

   ```bash
   python main.py
   ```

   ou

   ```bash
   python3 main.py
   ```

## Execution du script

Après avoir lancé le script main.py, des informations seront affichées dans la console, comprenant le titre des articles, la date de publication (correspondant à la date actuelle), ainsi que le résumé de chaque article généré par le modèle d'IA sélectionné. À la fin de l'exécution, tous les résumés des articles seront sauvegardés dans le dossier summary du projet (/summary/{nom_du_flux}/{date}/nom_de_l'article).

**Si vous souhaitez modifier deux paramètres dans le fichier main.py :**
Modifiez le nombre maximum d'articles pris en compte dans le résumé en ajustant la variable :

```bash
   num_articles_to_retrieve = 10
```

Vous pouvez également changer le modèle LLM en ajustant la variable model:

```bash
llm = Ollama(
    model="vicuna",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)
```

Enfin vous pouvez modifier le lien du flux rss en changeant la variable : 
```bash 
rss_link = "https://www.codesimplicity.com/feed/"
```

Bidault Romain MSI 5 - DEV A