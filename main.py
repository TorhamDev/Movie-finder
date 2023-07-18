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

    search_results = scraper.search_and_extract_data(movie_name)
    clear_terminal_screen()

    if not search_results:
        ShowMessage.nothing_found_message()
        quit()

    movies_link_page = dict()
    counter = 0
    for movie_name, movie_data in search_results.items():
        print(f"\n\t :movie_camera: {counter}. {movie_name}")
        movies_link_page[counter] = movie_data
        counter += 1

    choiced_link = int(Prompt.ask("\n :fire: pick one"))
    choiced_movie = movies_link_page[choiced_link]

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
