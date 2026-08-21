import os
import requests

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()                
TMDB_TOKEN = os.getenv("TMDB_TOKEN")

@app.get("/")

def home():         
    return {"message": "Movie Recommender API is running!"}           


def get_movie_id(movie_name: str):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if data.get("results"):
        first_movie = data["results"][0]
        return first_movie.get("id")
    return None

def get_movie_recommendations(movie_id: int):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    titles = []
    if data.get("results"):

        for movie in data["results"][:5]:
            titles.append(movie.get("title"))

    return titles

@app.get("/recommend") 

def get_recommendations(movie: str):
    
    movie_id = get_movie_id(movie)
    
    if movie_id is None:
        return {"error": f"Could not find any movie named '{movie}'"}
    
    recommended_titles = get_movie_recommendations(movie_id)
    
    return {"movie_searched": movie,
            "recommendations": recommended_titles
        }