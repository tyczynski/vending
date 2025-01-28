from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from typing import TypedDict, List, Dict, Any, Tuple
import requests
from datetime import datetime

class Article(TypedDict):
    title: str
    link: str
    description: str
    pubdate: datetime

class FeedScraper(ABC):
    def __init__(self, url: str) -> None:
        self.url = url

    def _scrape_blog(self) -> BeautifulSoup:
        response = requests.get(self.url)
        return BeautifulSoup(response.content, 'html.parser')
    
    @abstractmethod
    def get_articles(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_info(self) -> Tuple[str, str, str]:
        pass
