from restcountries import RestCountryApiV2 as rapi
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image


def main():
    # Grab India Flag
    india_flag_remote = rapi.get_country_by_country_code('IN').flag
    india_flag_local_svg = 'tmp/india.svg'
    india_flag_local_png = 'tmp/india.png'
    urllib.request.urlretrieve(india_flag_remote, india_flag_local_svg)
    renderPM.drawToFile(svg2rlg(india_flag_local_svg), india_flag_local_png, fmt='PNG')
    india_flag_pil = Image.open(india_flag_local_png)
    print(india_flag_pil)

if __name__ == '__main__':
    main()
