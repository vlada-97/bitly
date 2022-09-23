from dotenv import load_dotenv, find_dotenv
import requests
import os
from requests.exceptions import HTTPError
import argparse


load_dotenv()


def shorten_link(bitly_token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': "Bearer {}".format(bitly_token)
    }
    params = {
        "long_url": url
    }
    response = requests.post(bitly_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(bitly_token, link):
    click_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'.format(bitlink=link)
    headers = {
        'Authorization': "Bearer {}".format(bitly_token)
    }
    total_clicks = {
        "units": -1,
        "unit": "month"
    }
    response = requests.get(click_url, params=total_clicks, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitly_token, url):
    url_check_bitlink = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url)
    headers = {"Authorization": "Bearer {}".format(bitly_token)}
    response = requests.get(url_check_bitlink, headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type= str)
    args = parser.parse_args()


    bitly_token = '17c09e22ad155405159ca1977542fecf00231da7'
    url = args.url

    try: 
        if is_bitlink(bitly_token, url):
            print("Переходов по ссылке:{}".format(count_clicks(bitly_token, url)))
        else:
                print(shorten_link(bitly_token, url))
    except HTTPError:
        print("Неправильная ссылка: ", url)



if __name__ == "__main__":
    main()
