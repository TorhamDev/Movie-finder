from pydantic import BaseModel, HttpUrl


class MovieData(BaseModel):
    movie_link: HttpUrl
    movie_discription: str


class MovieExtractedData(BaseModel):
    movie_name: MovieData


class MovieLinksInfo(BaseModel):
    quality_info: HttpUrl
