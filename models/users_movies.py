from pydantic import BaseModel
from api.models.users import Users
from api.models.movies import Movies

class UsersMovies(BaseModel):
    users: Users
    movies: Movies