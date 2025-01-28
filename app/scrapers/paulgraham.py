from datetime import datetime
from bs4 import BeautifulSoup, ResultSet
from typing import List, Dict, Any, Tuple
from .base import Article, FeedScraper

class PaulGrahamFeedScraper(FeedScraper):
    def __init__(self):
        super().__init__('https://paulgraham.com/articles.html')

    def get_articles(self) -> List[Article]:
        soup = self._scrape_blog()
        articles: List[Article] = []
        articles_table: BeautifulSoup = soup.find_all('table')[2]
        articles_table_items: ResultSet[BeautifulSoup] = articles_table.find_all('tr', valign='top')
        now = datetime.now()

        for item in articles_table_items:
            item = item.find('a')
            title = item.text
            href = item['href']
            link = f"https://paulgraham.com/{href}" if not href.startswith('http') else href

            article = Article(
                title=title,
                link=link,
                description="",
                pubdate=now
            )

            articles.append(article)

        return articles
    
    def get_info(self) -> Tuple[str, str, str]:
        return "Paul Graham", "https://paulgraham.com", "Essays by Paul Graham"
