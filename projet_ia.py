import feedparser
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import sqlite3
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

def create_table():
    connection = sqlite3.connect("articles.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def insert_title(title, content):
    connection = sqlite3.connect("articles.db")
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO articles (title, content) VALUES (?, ?);", (title, content))

    connection.commit()
    connection.close()

def fetch_rss_feed(link):
    feed = feedparser.parse(link)
    return feed.entries

def filter_articles_by_day(articles, target_date):
    filtered_articles = [article for article in articles if datetime.strptime(article.published, "%a, %d %b %Y %H:%M:%S %z").date() == target_date]
    return filtered_articles

def select_top_articles(articles, num_articles):
    sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x.published, "%a, %d %b %Y %H:%M:%S %z"), reverse=True)
    return sorted_articles[:num_articles]

def retrieve_content(article_link):
    try:
        # Envoyer une requête HTTP pour obtenir le contenu de la page
        response = requests.get(article_link)
        response.raise_for_status()

        # Utiliser BeautifulSoup pour parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver le texte de l'article (ajuster les sélecteurs en fonction de la structure HTML du site)
        article_title = soup.find('title').get_text(strip=True)

        return article_title

    except Exception as e:
        print(f"Erreur lors de la récupération du contenu de l'article : {e}")
        return None

llm = Ollama(
    model="vicuna",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

create_table()

target_date = datetime.now().date() - timedelta(days=1)

rss_link = "https://www.frandroid.com/feed"
num_articles_to_retrieve = 5

articles = fetch_rss_feed(rss_link)
filtered_articles = filter_articles_by_day(articles, target_date)
selected_articles = select_top_articles(filtered_articles, num_articles_to_retrieve)

for article in selected_articles:
    article_title = retrieve_content(article.link)
    content_summarized = llm("Here is an article title. I would like you to provide me with additional information based on this title, in order to create a short article on the subject of this title : " + article_title + "\n\n")
    insert_title(article_title, content_summarized)