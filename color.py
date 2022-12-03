import math

from PIL import ImageColor

from rgb_color import RGBColor


class Color:
    def __init__(self, div=None, color_hex: str = None, color_name: str = None, color_url: str = None):
        self.div = div
        self.hex = color_hex
        self.name = color_name
        self.url = color_url

    @property
    def color_hex(self):
        if not self.hex:
            self.hex = self.div.get('style').split(': ')[-1]
        return self.hex

    @property
    def color_name(self):
        if not self.name:
            self.name = self.div.findChild('span', recursive=True).text
        return self.name

    @property
    def color_url(self):
        if not self.url:
            self.url = self.div.findChild('a', recursive=True).get('href')
        return self.url

    @staticmethod
    def hex_to_rgb(color_hex: str) -> tuple:
        return ImageColor.getrgb(color_hex)

    def calculate_difference(self, other_color):
        r, g, b = self.hex_to_rgb(self.color_hex)
        other_r, other_b, other_g = self.hex_to_rgb(other_color.color_hex)
        return math.sqrt((r - other_r) ** 2 + (g - other_g) ** 2 + (b - other_b) ** 2)
