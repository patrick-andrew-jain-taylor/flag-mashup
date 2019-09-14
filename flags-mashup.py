from restcountries import RestCountryApiV2 as rapi
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image


def main():
    india_flag_remote = rapi.get_country_by_country_code('IN').flag
    india_flag_local_svg = 'tmp/india.svg'
    india_flag_local_png = 'tmp/india.png'
    urllib.request.urlretrieve(india_flag_remote, india_flag_local_svg)
    renderPM.drawToFile(svg2rlg(india_flag_local_svg), india_flag_local_png, fmt='PNG')
    india_flag_pil = Image.open(india_flag_local_png)
    india_flag_pil_horz = india_flag_pil.size[0]
    india_flag_pil_vert = india_flag_pil.size[1]
    india_flag_colors = india_flag_pil.getcolors(india_flag_pil_horz*india_flag_pil_vert)
    return india_flag_colors

if __name__ == '__main__':
    main()
