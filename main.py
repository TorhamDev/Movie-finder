from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

from models.tools import print_banner, clear_terminal
from models.messages import ShowMessage
from avamovie.scraper import AvaMovieScraper


def main():
    scraper = AvaMovieScraper()

    search_param = Prompt.ask(":sparkles: Search Movie Name")

    ShowMessage.searching()

    search_result = scraper.search_and_extract_data(search_param)
    clear_terminal()

    if not search_result:
        ShowMessage.nothing_found()
        quit()

    counter = 0
    links = dict()
    for result_key in list(search_result.keys()):
        print(f"\n\t :movie_camera: {counter}. {result_key}")
        links[counter] = result_key
        counter += 1

    choiced_link = Prompt.ask("\n :fire: pick one")
    choiced_movie = search_result[links[int(choiced_link)]]

    ShowMessage.searching_for_links()

    download_links = scraper.get_movie_download_links(
        choiced_movie["movie_link"]
    )

    clear_terminal()

    print(Panel(choiced_movie["movie_discription"]))

    for quality, download_link in download_links.items():
        print("\n:star2:", quality, "=>", download_link)


if __name__ == "__main__":
    print_banner()
    main()
