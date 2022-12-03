import requests
from bs4 import BeautifulSoup
from typing import List

from color import Color


class ColorFetcher:
    def __init__(self, url: str):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')

    def fetch_colors(self) -> List[Color]:
        color_divs = self.soup.findAll('div', {'class': 'palette-single-color'})
        return [Color(color_div) for color_div in color_divs]
