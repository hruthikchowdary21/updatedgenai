import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_jobs(base_url, max_jobs):
    jobs = []
    page = 1
    while len(jobs) < max_jobs:
        url = f"{base_url}&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            break  # Exit if there's an error loading the page

        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('div', class_='job-card')  # You need to verify the correct class name for job listings

        for card in job_cards:
            job_title = card.find('a', class_='job-link').text.strip()  # Adjust class if necessary
            company_name = card.find('a', class_='company-link').text.strip()  # Adjust class if necessary
            location = card.find('span', class_='job-location').text.strip()  # Adjust class if necessary

            jobs.append({
                'Title': job_title,
                'Company': company_name,
                'Location': location
            })

            if len(jobs) >= max_jobs:
                break

        page += 1

    return jobs

# URL setup with query parameters
base_url = "https://www.dice.com/jobs?q=data%20analyst&countryCode=US&radius=30&radiusUnit=mi&pageSize=20&language=en"

# Scrape the first 1000 jobs
jobs_data = fetch_jobs(base_url, 1000)

# Convert to DataFrame and save to CSV
jobs_df = pd.DataFrame(jobs_data)
jobs_df.to_csv('dice_jobs.csv', index=False)
