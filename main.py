from color import Color
from color_fetcher import ColorFetcher
from color_matcher import ColorMatcher


def main():
    url = 'https://tambour.co.il/color-fan/color-chart/'
    requested_color = Color(color_hex="#0F7B98")
    colors = ColorFetcher(url).fetch_colors()
    print(Color.hex_to_rgb('#0F7B98'))
    for color in colors:
        if color.color_name == "Clouded Cover":
            print(color.color_hex)
    color_matcher = ColorMatcher(colors)
    matched_color = color_matcher.match(requested_color)
    print(matched_color.color_url)


if __name__ == '__main__':
    main()
