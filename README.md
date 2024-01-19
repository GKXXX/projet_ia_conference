# Projet IA Veille Technologique

Ce projet en Python a pour objectif de récupérer des articles via un flux RSS et, à l'aide d'un modèle de Langage de Modélisation (LLM) en intelligence artificielle, de générer un résumé pour chaque article. Ce projet doit être installé et éxécuté sur une marchine virtuelle Ubuntu.

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

#  
Mettez en place SQLite3 pour la gestion du stockage des articles

- Obtenez le fichier précompilé de SQLite pour Windows en le téléchargeant depuis le site officiel SQLite: https://www.sqlite.org/download.html
- Intégrez une nouvelle variable d'environnement système dans le PATH de Windows. Cette variable doit pointer vers le répertoire où se trouvent les outils SQLite précompilés (sqlite-tools-win-x64).



## Execution du script

Après avoir lancé le script main.py, des informations seront stockées dans la base de donnée. Vous pourrez ensuite via des requêtes sql, accéder aux différents résumés des différents articles agrégés par le script avec des requêtes du type : 
```SQL
   SELECT title,content FROM articles;
   ```

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