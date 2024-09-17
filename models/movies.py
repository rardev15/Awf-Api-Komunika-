from typing import Union
from pydantic import BaseModel

class Movies(BaseModel):
    movie_id: int
    movie_name: str | max = 50