# this file loads feeds using rss from links in config.py

import feedparser
from config import RSS_FEEDS

def get_news():

    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for item in feed.entries:
            articles.append({
                "title": item.title
                #"summary": item.summary
            })

    return articles