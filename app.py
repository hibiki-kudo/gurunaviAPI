import os

from search import search_restaurants

URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

KEY_ID = os.environ["key_id"]


def main():
    freeword = "寿司"
    restaurants = search_restaurants(
        URL,
        KEY_ID,
        freeword
    )
    for restaurant in restaurants:
        print(restaurant.get_shop_info())


if __name__ == "__main__":
    main()
