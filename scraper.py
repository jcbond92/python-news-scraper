import requests
from bs4 import BeautifulSoup
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def scrapeText(config):
    data = []
    print(config['name'])

    response = requests.get(
        url=config['url'],
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    textItems = soup.select(config['cssSelector'])
    for textItem in textItems:
        textData = textItem.text.strip()
        analysis = sia.polarity_scores(textData)
        text = {
            "textData": textData,
            "analysis": analysis
        }
        data.append(text)

    fileName = config['name'] + '.json'

    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)


# add more pages here
pages = [
    {
        "url": "https://www.washingtonpost.com",
        "name": "wash-post-homepage-headlines",
        "cssSelector": "h2"
    },
    {
        "url": "https://www.washingtonpost.com/us-policy/2021/10/04/biden-schumer-debt-ceiling/",
        "name": "wash-post-debt-ceiling",
        "cssSelector": "section"
    }
]

for page in pages:
    scrapeText(page)
