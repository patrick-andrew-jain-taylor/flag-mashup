from restcountries import RestCountryApiV2 as rapi
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image

COUNTRY_CODES = {
    'India': 'IN',
    'United States': 'US'
}


def country_flag_colors(country):
    flag_remote = rapi.get_country_by_country_code(COUNTRY_CODES.get(country.title())).flag
    flag_local_svg = 'tmp/{}.svg'.format(country.lower())
    flag_local_png = 'tmp/{}.png'.format(country.lower())
    urllib.request.urlretrieve(flag_remote, flag_local_svg)
    renderPM.drawToFile(svg2rlg(flag_local_svg), flag_local_png, fmt='PNG')
    flag_pil = Image.open(flag_local_png)
    flag_pil_horz = flag_pil.size[0]
    flag_pil_vert = flag_pil.size[1]
    flag_colors = flag_pil.getcolors(flag_pil_horz*flag_pil_vert)
    return flag_colors


if __name__ == '__main__':
    india_flag_colors = country_flag_colors('India')
    us_flag_colors = country_flag_colors('United States')
