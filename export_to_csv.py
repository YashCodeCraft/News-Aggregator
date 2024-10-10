import csv
from db_setup import Article, session

def export_to_csv(filename='articles.csv'):
    articles = session.query(Article).all()
    
    # Open a CSV file for writing
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Title', 'Link', 'Published Date', 'Summary', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write article data row by row
        for article in articles:
            writer.writerow({
                'ID': article.id,
                'Title': article.title,
                'Link': article.link,
                'Published Date': article.published,
                'Summary': article.summary,
                'Category': article.category
            })

    print(f"Data exported to {filename}")

# Run the export function
export_to_csv()
