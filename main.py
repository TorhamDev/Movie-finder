from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

from models.tools import print_banner, clear_terminal
from avamovie.scraper import AvaMovieScraper


print_banner()


search_param = name = Prompt.ask(":sparkles: Search Movie Name")

scraper = AvaMovieScraper()

print("\n\n:tractor:[deep_pink1] Searching...[/deep_pink1]")

search_result = scraper.search_and_extract_data(search_param)

clear_terminal()

result_keys = list(search_result.keys())


if len(result_keys) == 0:
    print("\n\n\t\t :no_entry_sign: Nothing found :flushed:")
    quit()

counter = 0
for result_key in result_keys:
    print(f"\n\t :movie_camera: {counter}. {result_key}")
    counter += 1

choiced_link = Prompt.ask("\n :fire: pick one")

choiced_movie = search_result[result_keys[int(choiced_link)]]

print(Panel(choiced_movie["movie_discription"]))

print("\n\n:tractor:[deep_pink1] Searching for download links...[/deep_pink1]")

download_links = scraper.get_movie_download_links(choiced_movie["movie_link"])

clear_terminal()

for quality, download_link in download_links.items():
    print(quality, "=>", download_link)
