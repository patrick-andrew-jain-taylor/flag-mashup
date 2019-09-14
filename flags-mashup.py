from restcountries import RestCountryApiV2 as rapi


def main():
    # Grab India & US Flags
    india_flag = rapi.get_country_by_country_code('IN').flag
    united_states_flag = rapi.get_country_by_country_code('US').flag


if __name__ == '__main__':
    main()
