import requests
from bs4 import BeautifulSoup
import csv
import time

def fetch_page(url):
    """Fetches a webpage and returns a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_page(soup):
    """Parses the BeautifulSoup object and returns a list of dictionaries containing book data."""
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']  # Extract book title
        price = book.find('p', class_='price_color').text.strip()  # Extract book price
        books.append({'title': title, 'price': price})
    return books

def save_to_csv(data, filename):
    """Saves the list of dictionaries to a CSV file."""
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

# Example usage
url = 'http://books.toscrape.com/'  # Example URL
soup = fetch_page(url)
if soup:
    book_data = parse_page(soup)
    save_to_csv(book_data, 'books.csv')
    print("Data saved to books.csv")
else:
    print("Failed to fetch or parse the page.")
