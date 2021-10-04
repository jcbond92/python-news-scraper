from app.scraper import scrapeText

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
