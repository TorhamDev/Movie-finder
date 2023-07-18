from bs4 import BeautifulSoup
import requests


class AvaMovieScraper:
    """
    Scraper class for avamovie website scraber
    """

    def get_movie_download_links(self, download_page_link: str) -> dict:
        """
        Scraping movie download page and extracing movie download links

        param : movie download page link

        retrun: movie links in different qualities
        """
        data = requests.get(download_page_link, allow_redirects=False).content
        soup = BeautifulSoup(data, features="lxml")
        links_data = soup.find_all("div", class_="row_data")
        result = dict()

        for link in links_data:
            if "نیازمند اشتراک" not in link.text:
                download_link = link.find(
                    "a",
                    class_="siteSingle__boxContent__downloadContent__link"
                )["href"]

                quality_info = link.find("div", class_="quality")
                subtilte_status = ""
                if quality_info.span:
                    subtilte_status = f"[{quality_info.span.text}]"
                quality_info = self._clean_text(
                    quality_info.text.replace(subtilte_status, "")
                ).replace(" ", "")
                quality_info = f"{quality_info} {subtilte_status}"

                result[quality_info] = download_link

        return result

    def search(self, search_param: str) -> list:
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
            search_result = soup.find_all("article", class_="sitePost")
            [all_results.append(i) for i in search_result]
            if len(search_result) < 10:
                break

            start_page += 1

        return all_results

    def extract_search_data(self, search_results: list) -> dict:
        """
        extracting data from the bs4 objects we got from search funtion

        search_result : list of bs4 search result from avamovie

        retrun : dict of {
        
            movie_name : {
                "movie_link": movie_link,
                "movie_cover_link": movie_cover_link,
                "movie_discription": discription, 
            }
            ...
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

    def search_and_extract_data(self, search_param: str) -> dict:

        search_results = self.search(search_param)
        extracted_data = self.extract_search_data(search_results)

        if len(extracted_data.keys()) == 0:
            return False

        return extracted_data

    def _clean_text(self, text: str) -> str:
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
        ).replace(
            "\r",
            " "
        )

        return text
