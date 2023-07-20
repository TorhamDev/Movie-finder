from pydantic import BaseModel, HttpUrl
from typing import Dict


class Movie(BaseModel):
    movie_link: HttpUrl
    movie_discription: str


class MovieExtractedData(BaseModel):
   movies: Dict[str, Movie]


class MovieLinksInfo(BaseModel):
    quality_info: HttpUrl
