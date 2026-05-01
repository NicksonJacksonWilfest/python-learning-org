
import requests
from bs4 import BeautifulSoup

def get_nyt_titles():
    url = 'https://www.nytimes.com/'

    # We include a 'User-Agent' header so the website doesn't instantly block us
    # for looking like an automated bot.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 1. Request the HTML from the NYT homepage
    response = requests.get(url, headers=headers)

    # 2. Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Find the titles.
    # NYT usually puts their article headlines inside <h2> or <h3> tags.
    # We use find_all to grab a list of all these elements.
    headlines = soup.find_all(['h2', 'h3'])

    # 4. Loop through the elements and print the text inside them
    print("--- New York Times Homepage Titles ---")
    for headline in headlines:
        # .get_text() extracts the string inside the HTML tag
        # .strip() removes any accidental spaces or newlines at the beginning/end
        title_text = headline.get_text().strip()

        # Some empty tags might get picked up, so we check if title_text actually has content
        if title_text:
            print(f"- {title_text}")

if __name__ == '__main__':
    get_nyt_titles()
