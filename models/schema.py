from pydantic import BaseModel, HttpUrl


class Movie(BaseModel):
    movie_link: HttpUrl
    movie_discription: str


class MovieExtractedData(BaseModel):
   movies: dict[str, Movie]


class MovieLinksInfo(BaseModel):
    quality_info: HttpUrl
