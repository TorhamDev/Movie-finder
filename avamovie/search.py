from bs4 import BeautifulSoup
import requests


def clean_text(text: str) -> str:
    text = text.replace(
        "\t",
        " "
    ).replace(
        "\u200e",
        " "
    ).replace(
        "\u200c",
        " "
    ).replace(
        "\n",
        " "
    )

    return text


def search(search_param: str):
    start_page = 1

    all_results = list()

    while True:
        url = (
            "https://avamovie2.info/page/{}/?s={}".format(
                start_page,
                search_param,
            )
        )
        data = requests.get(url, allow_redirects=False).content
        soup = BeautifulSoup(data, features="lxml")
        names = soup.find_all("article", class_="sitePost")
        [all_results.append(i) for i in names]
        if len(names) < 10:
            break

        start_page += 1

    return all_results


def extract_search_data(search_results: list):

    results = dict()

    for data in search_results:

        discription = clean_text(data.find("div", class_="plot").text)

        movie_name = data.div.div.figure.a["title"]
        movie_link = data.div.div.figure.a["href"]
        movie_cover_link = data.div.div.figure.a.img["src"]
        results[movie_name] = {
            "movie_link": movie_link,
            "movie_cover_link": movie_cover_link,
            "movie_discription": discription,
        }

    return results


print(extract_search_data(search("batman")))
