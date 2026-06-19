from pydantic import BaseModel


class Article(BaseModel):
    title : str
    description : str | None = None
    url : str