from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

from models.tools import print_banner, clear_terminal_screen
from models.messages import ShowMessage
from avamovie.scraper import AvaMovieScraper

scraper = AvaMovieScraper()


def main() -> None:
    """
    Get the name of the movie and search it by scraper and find the links to download the movie
    """

    movie_name = Prompt.ask(":sparkles: Enter Movie Name")

    ShowMessage.searching_message()

    search_result = scraper.search_and_extract_data(movie_name)
    clear_terminal_screen()

    if not search_result:
        ShowMessage.nothing_found_message()
        quit()

    movie_page_links = dict()
    for number, movie_name in enumerate(search_result.keys()):
        print(f"\n\t :movie_camera: {number}. {movie_name}")
        movie_page_links[number] = movie_name

    choiced_link = Prompt.ask("\n :fire: pick one")
    choiced_movie = search_result[movie_page_links[int(choiced_link)]]

    ShowMessage.searching_for_links_message()

    download_links = scraper.get_movie_download_links(
        choiced_movie["movie_link"]
    )

    clear_terminal_screen()

    print(Panel(choiced_movie["movie_discription"]))

    for quality, download_link in download_links.items():
        print("\n:star2:", quality, ":", download_link)


if __name__ == "__main__":
    print_banner()
    main()
