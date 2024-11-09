import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """Fetches a webpage and returns a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_links(soup):
    """Extracts all hyperlinks from the BeautifulSoup object."""
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Ensure the link is absolute
        if not href.startswith('http'):
            href = requests.compat.urljoin(url, href)
        links.append(href)
    return links

def save_links_to_file(links, filename):
    """Saves the list of links to a text file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

# Example usage
url = 'http://books.toscrape.com/'  # Example URL
soup = fetch_page(url)
if soup:
    links = extract_links(soup)
    save_links_to_file(links, 'sublinks.txt')
    print("Links saved to sublinks.txt")
else:
    print("Failed to fetch or parse the page.")