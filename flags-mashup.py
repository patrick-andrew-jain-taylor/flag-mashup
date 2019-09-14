from restcountries import RestCountryApiV2 as rapi
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image

COUNTRY_CODES = {
    'India': 'IN',
    'United States': 'US'
}


def country_flag(country):
    flag_remote = rapi.get_country_by_country_code(COUNTRY_CODES.get(country.title())).flag
    flag_local_svg = 'tmp/{}.svg'.format(country.lower())
    flag_local_png = 'tmp/{}.png'.format(country.lower())
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
    india_flag = country_flag('India')
    us_flag = country_flag('United States')
    india_flag_colors = sorted(country_flag_colors(india_flag), reverse=True)
    us_flag_colors = sorted(country_flag_colors(us_flag), reverse=True)
    print(len(india_flag_colors), len(us_flag_colors))


if __name__ == '__main__':
    main()
