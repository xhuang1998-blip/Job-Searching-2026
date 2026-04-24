import requests
from bs4 import BeautifulSoup
import json

# Constants
BASE_URLS = {
    'indeed': 'https://www.indeed.com/jobs',
    'linkedin': 'https://www.linkedin.com/jobs',
    'craigslist': 'https://boston.craigslist.org/search/jjj',
}

# Function to scrape job postings from Indeed

def scrape_indeed(location, keywords):
    params = {'q': keywords, 'l': location}
    response = requests.get(BASE_URLS['indeed'], params=params)
    jobs = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for card in job_cards:
            title = card.find('h2').text.strip()
            company = card.find('span', class_='company').text.strip()
            jobs.append({'title': title, 'company': company})
    else:
        print(f'Error fetching Indeed jobs: {response.status_code}')
    return jobs

# Function to scrape job postings from LinkedIn

def scrape_linkedin(location, keywords):
    # Similar approach to scrape LinkedIn jobs
    # ...
    pass

# Function to scrape job postings from Craigslist

def scrape_craigslist(location, keywords):
    # Similar approach to scrape Craigslist jobs
    # ...
    pass

# Function to store results in JSON file

def store_results(jobs, filename):
    with open(filename, 'w') as file:
        json.dump(jobs, file, indent=4)

# Main script logic
if __name__ == '__main__':
    location = 'Boston, Massachusetts'
    keywords = 'fintech operations IT finance'
    all_jobs = []
    all_jobs.extend(scrape_indeed(location, keywords))
    all_jobs.extend(scrape_linkedin(location, keywords))
    all_jobs.extend(scrape_craigslist(location, keywords))
    store_results(all_jobs, 'job_postings.json')
    print('Job postings scraped and stored successfully!')