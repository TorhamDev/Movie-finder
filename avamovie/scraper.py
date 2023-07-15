from bs4 import BeautifulSoup
import requests


class AvaMovieScraper:
    """
    Scraper class for avamovie website scraber
    """

    def search(search_param: str) -> list:
        """
        The search scraper for avamovie search

        param : search_param : what you want search in avamovie?

        retrun : list of bs4 object from search result
        """
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

    def extract_search_data(self, search_results: list) -> dict:
        """
        extracting data from the bs4 objects we got from search funtion

        search_result : list of bs4 search result from avamovie

        retrun : dict of {movie_name : {
                "movie_link": movie_link,
                "movie_cover_link": movie_cover_link,
                "movie_discription": discription, 
            }
        }
        """
        results = dict()

        for data in search_results:

            discription = self._clean_text(
                data.find("div", class_="plot").text)

            movie_name = data.div.div.figure.a["title"]
            movie_link = data.div.div.figure.a["href"]
            movie_cover_link = data.div.div.figure.a.img["src"]
            results[movie_name] = {
                "movie_link": movie_link,
                "movie_cover_link": movie_cover_link,
                "movie_discription": discription,
            }

        return results

    def _clean_text(text: str) -> str:
        """
        Cleaning extra chars from persian sentence we got in search result

        param : text : persian text for cleaning

        return : cleaned text
        """
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
