import requests
from bs4 import BeautifulSoup
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from app.cloudgenerator import createWordCloud
import os


nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def scrapeText(config):
    data = []
    rawText = []
    print(config['name'])

    response = requests.get(
        url=config['url']
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
        rawText.append(textData)
        data.append(text)

    # create file path to write json
    script_dir = os.path.dirname(__file__)
    rel_path = 'results/' + config['name'] + '.json'
    abs_file_path = os.path.join(script_dir, rel_path)

    # write the json
    with open(abs_file_path, 'w') as outfile:
        json.dump(data, outfile)

    print("completed sentiment analysis")

    # create the word cloud
    wordCloudConfig = {
        'name': config['name'],
        'text': rawText
    }

    createWordCloud(wordCloudConfig)
