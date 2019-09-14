from restcountries import RestCountryApiV2 as rapi
import urllib.request

def main():
    # Grab India Flag
    india_flag_remote = rapi.get_country_by_country_code('IN').flag
    india_flag_local = 'tmp/india.svg'
    urllib.request.urlretrieve(india_flag_remote, india_flag_local)


if __name__ == '__main__':
    main()
