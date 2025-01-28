from typing import List, Dict, Any
from feedgenerator import Rss201rev2Feed

def create_rss_feed(title: str, link: str, description: str, items: List[Dict[str, Any]]) -> Rss201rev2Feed:
    feed = Rss201rev2Feed(
        title=title,
        link=link,
        description=description
    )

    for item in items:
        feed.add_item(
            title=item['title'],
            link=item['link'],
            description=item['description'],
            pubdate=item['pubdate']
        )

    return feed
