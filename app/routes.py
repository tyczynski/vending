from flask import Response
from .scrapers.paulgraham import PaulGrahamFeedScraper
from .utils.feed import create_rss_feed

WEBSITES = {
    "paulgraham": PaulGrahamFeedScraper()
}

def generate_feed(id: str):
    if id not in WEBSITES:
        return "Website not supported", 404

    scraper = WEBSITES[id]
    items = scraper.get_articles()
    title, link, description = scraper.get_info()

    feed = create_rss_feed(title, link, description, items)

    return Response(
        feed.writeString('utf-8'),
        mimetype='application/xml'
    )
