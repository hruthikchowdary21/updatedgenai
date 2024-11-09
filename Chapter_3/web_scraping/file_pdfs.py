import requests
from fpdf import FPDF
from bs4 import BeautifulSoup
import os

def fetch_page_content(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_text_from_html(html_content):
    """Extracts visible text from HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    # Get text from all paragraphs and headings
    text = ' '.join(soup.stripped_strings)
    return text

def save_content_to_pdf(content, filename):
    """Saves the given content to a PDF file."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Split content into lines and add to PDF
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, txt=line)
    
    pdf.output(filename)

def process_links_from_file(filename):
    """Reads links from a text file and saves each page's content to a PDF."""
    with open(filename, 'r', encoding='utf-8') as file:
        links = file.readlines()
    
    for i, link in enumerate(links, start=1):
        link = link.strip()
        html_content = fetch_page_content(link)
        if html_content:
            text_content = extract_text_from_html(html_content)
            pdf_filename = f'page_{i}.pdf'
            save_content_to_pdf(text_content, pdf_filename)
            print(f"Content from {link} saved to {pdf_filename}")

# Example usage
links_file = 'sublinks.txt'  # The text file containing the links
process_links_from_file(links_file)
