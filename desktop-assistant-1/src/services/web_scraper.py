import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        pass

    def scrape(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to fetch the webpage")

    def parse_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        data = []
        for item in soup.find_all('p'):
            data.append(item.text)
        return data

    def save_data(self, data, filename):
        with open(filename, 'w') as file:
            for item in data:
                file.write(f"{item}\n")