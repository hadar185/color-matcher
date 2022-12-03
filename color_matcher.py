from typing import List

from color import Color


class ColorMatcher:
    def __init__(self, colors: List[Color]):
        self.colors = colors

    def match(self, requested_color: Color) -> Color:
        return min(self.colors, key=lambda color: color.calculate_difference(requested_color))
