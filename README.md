# News Aggregator and Classifier

## 1.Project Overview
This project is designed to collect news articles from various RSS feeds, store them in a MySQL database, and categorize them into predefined categories such as:
- **Terrorism / Protest / Political Unrest / Riot**
- **Positive / Uplifting**
- **Natural Disasters**
- **Others**

The project utilizes Python for data extraction, Celery for task management, and NLP (via spaCy) for categorization.

## Technologies and Libraries Used
- **Python**: Primary programming language for the project.
- **MySQL**: Relational database used to store articles.
- **Celery**: Used to handle asynchronous tasks (processing news articles).
- **Redis**: Message broker for Celery.
- **spaCy**: NLP library for classifying news articles.
- **Feedparser**: To parse RSS feeds.
- **SQLAlchemy**: ORM used for interacting with the MySQL database.

## Installation and Setup Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/your-username/rss_project.git
cd rss_project
```

## 2. Set Up the Virtual Environment (Optional)
It’s recommended to create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```


