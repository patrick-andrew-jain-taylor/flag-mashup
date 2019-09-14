from restcountries import RestCountryApiV2 as rapi
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image
from collections import namedtuple
import os
import shutil

COUNTRY_CODES = {
    'India': 'IN',
    'United States': 'US'
}

COLOR_GET = namedtuple('COLOR_GET', 'count RGB')


def country_flag(country):
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    country_code = COUNTRY_CODES.get(country.title())
    flag_remote = rapi.get_country_by_country_code(COUNTRY_CODES.get(country.title())).flag
    flag_local_svg = 'tmp/{}.svg'.format(country_code)
    flag_local_png = 'tmp/{}.png'.format(country_code)
    urllib.request.urlretrieve(flag_remote, flag_local_svg)
    renderPM.drawToFile(svg2rlg(flag_local_svg), flag_local_png, fmt='PNG')
    flag_pil = Image.open(flag_local_png)
    return flag_pil


def country_flag_colors(flag_pil):
    flag_pil_horz = flag_pil.size[0]
    flag_pil_vert = flag_pil.size[1]
    flag_colors = flag_pil.getcolors(flag_pil_horz*flag_pil_vert)
    return flag_colors


def main():
    if not os.path.exists('swaps'):
        os.makedirs('swaps')
    country_one = 'India'
    country_one_code = COUNTRY_CODES.get(country_one.title())
    country_one_flag = country_flag(country_one)
    country_one_flag_colors = sorted(country_flag_colors(country_one_flag), reverse=True)
    country_one_flag_colors_swap = [COLOR_GET(*color) for color in country_one_flag_colors[:3]]
    country_two = 'United States'
    country_two_code = COUNTRY_CODES.get(country_two.title())
    country_two_flag = country_flag(country_two)
    country_two_flag_colors = sorted(country_flag_colors(country_two_flag), reverse=True)
    country_two_flag_colors_swap = [COLOR_GET(*color) for color in country_two_flag_colors[:3]]
    # Remove Identical colors
    remove_identical_colors(country_one_flag_colors_swap, country_two_flag_colors_swap)
    # Swap pixels
    swap_pixels_and_save(country_one_code, country_two_code, country_one_flag, country_one_flag_colors_swap, country_two_flag_colors_swap)
    swap_pixels_and_save(country_two_code, country_one_code, country_two_flag, country_two_flag_colors_swap, country_one_flag_colors_swap)
    # Clean up
    shutil.rmtree('tmp')
    country_one_flag.close()
    country_two_flag.close()


def swap_pixels_and_save(country_code_one, country_code_two, country_one_flag, country_one_colors_swap, country_two_colors_swap):
    flag_pixels = country_one_flag.load()
    swap_png = 'swaps/{}-to-{}-swap.png'.format(country_code_one, country_code_two)
    width, height = country_one_flag.size
    for x in range(width):
        for y in range(height):
            for color in country_one_colors_swap:
                r, g, b = flag_pixels[x, y]
                if (r, g, b) == color.RGB:
                    flag_pixels[x, y] = country_two_colors_swap[country_one_colors_swap.index(color)].RGB
    country_one_flag.save(swap_png)


def remove_identical_colors(india_flag_colors_swap, us_flag_colors_swap):
    for india_color in india_flag_colors_swap:
        for us_color in us_flag_colors_swap:
            if india_color.RGB == us_color.RGB:
                india_flag_colors_swap.remove(india_color)
                us_flag_colors_swap.remove(us_color)


if __name__ == '__main__':
    main()
