import feedparser
import spacy
from db_setup import Article, session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the NLP model
nlp = spacy.load('en_core_web_sm')

categories = {
    'Terrorism / Protest / Political Unrest / Riot': ['terrorism', 'protest', 'riot', 'political unrest', 'insurgency', 'demonstration', 'clash', 'rebellion'],
    'Positive/Uplifting': ['positive', 'uplifting', 'inspiring', 'motivational', 'encouraging', 'heartwarming', 'optimistic', 'joyful'],
    'Natural Disasters': ['earthquake', 'flood', 'storm', 'disaster', 'hurricane', 'tornado', 'tsunami', 'landslide', 'wildfire', 'volcano'],
    'Others': []
}

def classify_article(text):
    doc = nlp(text.lower())
    for category, keywords in categories.items():
        if any(keyword in doc.text for keyword in keywords):
            return category
    return 'Others'

def save_article(article_data):
    try:
        # Check for duplicates by link
        if session.query(Article).filter_by(link=article_data['link']).first():
            logging.info(f"Duplicate article: {article_data['title']}")
            return

        # Classify the article
        category = classify_article(article_data['summary'])

        # Create and save the Article
        article = Article(
            title=article_data['title'],
            link=article_data['link'],
            published=datetime.strptime(article_data['published'], '%a, %d %b %Y %H:%M:%S %Z'),
            summary=article_data['summary'],
            category=category
        )

        session.add(article)
        session.commit()
        logging.info(f"Article saved: {article_data['title']}")

    except IntegrityError as e:
        session.rollback()  # Rollback the session in case of an error
        logging.error(f"Error saving article: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def fetch_rss_feed(url):
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            article_data = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if 'published' in entry else 'No publication date',
                'summary': entry.summary if 'summary' in entry else 'No summary available',
            }
            save_article(article_data)
    except Exception as e:
        logging.error(f"Error fetching feed {url}: {e}")

# Example usage
if __name__ == "__main__":
    feed_urls = [
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://qz.com/feed",
        "http://feeds.foxnews.com/foxnews/politics",
        "http://feeds.reuters.com/reuters/businessNews",
        "http://feeds.feedburner.com/NewshourWorld",
        "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
    ]

    for feed_url in feed_urls:
        fetch_rss_feed(feed_url)



