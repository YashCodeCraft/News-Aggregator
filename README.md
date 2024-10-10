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
git clone https://github.com/YashCodeCraft/News-Aggregator.git
cd rss_project
```

## 2. Set Up the Virtual Environment (Optional)
It’s recommended to create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

## 3. Install the Required Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

## 4. Set Up the MySQL Database
1. Install MySQL if you don’t already have it installed.
2. Open MySQL Workbench and run the following commands to create the database and user:
```sql
CREATE DATABASE 'new_database';
CREATE USER 'your_user_name'@'localhost' IDENTIFIED BY 'Your Password';
GRANT ALL PRIVILEGES ON 'new_database'.* TO 'your_user_name'@'localhost';
FLUSH PRIVILEGES;
```
3. After that, make sure the database is ready to accept connections.

## 5. Run Database Setup Script
Run the `db_setup.py` file to create the `articles` table in your MySQL database:
```bash
python db_setup.py
```

## 6. Run Redis
Ensure Redis is installed and running on your local machine (Install it first). To start Redis:
```bash
redis-server
```

## 7. Start Celery Worker
Start the Celery worker for asynchronous processing of RSS feeds:
```bash
celery -A celery_config worker --loglevel=info
```

## 8. Run the RSS Extraction Script
To fetch and process articles from the provided RSS feeds, run:
```bash
python rss_extract.py
```
This will extract news articles from the feeds, classify them using NLP, and store them in the database.

## 9. Exporting Data to CSV
After processing RSS feeds and storing the articles in the database, you can export the articles to a CSV file by running:

```bash
python export_to_csv.py
```

## 10. Viewing the Data in MySQL
To view the saved articles, open MySQL Workbench and run:
```sql
USE news_db;
SELECT * FROM articles;
```

## Database Schema
The MySQL database contains the following columns in the `articles` table:

- id: Unique identifier for each article.
- title: The title of the news article (unique).
- link: URL to the full article.
- published: The publication date of the article.
- summary: A short summary of the article.
- category: The classified category of the article.

## How the Project Works
1. **RSS Parsing:** The `feedparser` library parses RSS feeds to extract the article's title, link, publication date, and summary.
2. **NLP Classification:** The article summary is classified into categories (Terrorism, Uplifting, Natural Disasters, Others) using the `spaCy` NLP model.
3. **Celery for Asynchronous Processing:** Articles are processed asynchronously using Celery workers to ensure non-blocking operation when fetching from multiple RSS feeds.
4. **Database Storage:** Each classified article is stored in a MySQL database, avoiding duplicates by checking for existing articles based on their unique link.  


## Logging and Error Handling
The project uses Python's built-in logging module to track events and handle errors:
- Logs successful article saving and error messages during saving operations.
- Gracefully handles network issues or issues with RSS feeds by logging errors.

## Assumptions
- The RSS feeds will be in English.
- The feeds will follow a common structure, though minor variations are accounted for in the parsing logic.
- Redis and MySQL are properly installed and configured.

  
## Notes
- You can modify the list of RSS feeds in the `rss_extract.py` file by adding new URLs.
- Make sure to restart the Celery worker after any significant changes to the project code.

