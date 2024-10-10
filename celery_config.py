from celery import Celery
from rss_extract import save_article

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_article(article_data):
    try:
        save_article(article_data)
    except Exception as e:
        logging.error(f"Error processing article: {e}")
