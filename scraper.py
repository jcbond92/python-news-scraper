import requests
from bs4 import BeautifulSoup


def scrapeNewsHeadline(url):
    response = requests.get(
        url='https://www.' + url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    mainHeadlines = soup.select('h2')
    for mainHeadline in mainHeadlines:
        print(mainHeadline.text.strip())

    subHeadlines = soup.select('h3')
    for subHeadline in subHeadlines:
        print(subHeadline.text.strip())


sites = ["nytimes.com", "washingtonpost.com"]
for site in sites:
    scrapeNewsHeadline(site)
