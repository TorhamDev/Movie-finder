from rich import print
from rich.prompt import Prompt

from models.tools import print_banner
from avamovie.scraper import AvaMovieScraper


print_banner()


search_param = name = Prompt.ask(":sparkles: Search Movie Name")

scraper = AvaMovieScraper()

print("\n\n:tractor:[deep_pink1] Searching...[/deep_pink1]")


search_result = scraper.search_and_extract_data(search_param)

print(search_result)