# Python News Scraper

A simple python scraper that grabs text off of news sites for sentiment analysis and creates a word cloud.

## Running the script

This script relies on the `matplotlib`, `wordcloud`, `requests`, `BeautifulSoup`, `json`, and `nltk` packages.

```
git clone https://github.com/jcbond92/python-news-scraper.git
cd python-news-scraper
pip install matplotlib wordcloud requests BeautifulSoup json nltk
python run.py
```

Files will be output to the `app/results` subdirectory.

## Editing the pages that are analyzed

In `run.py` you can update the configuration with more pages:

```python
pages = [
    {
        "url": "https://www.washingtonpost.com", # path of the page to request
        "name": "wash-post-homepage-headlines", # a name that will be used when the output files are created
        "cssSelector": "h2" # the CSS selector used to grab the text for evaluation (this is grabs all instances of that element)
    },
    {
        "url": "https://www.washingtonpost.com/us-policy/2021/10/04/biden-schumer-debt-ceiling/",
        "name": "wash-post-debt-ceiling",
        "cssSelector": "section"
    }
]
```
