from django.http import JsonResponse
import pickle, os, requests, pandas as pd

movies_dict_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies_dict.pkl')
similarity_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'similarity.pkl')
with open(movies_dict_path, 'rb') as file: movies_dict = pickle.load(file)
with open(similarity_path, 'rb') as file: similarity = pickle.load(file)
movies = pd.DataFrame(movies_dict)
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2I0MDY1NGI2NzhlODA4NDU0ZjQ1ZTkyMDMzZTE3YSIsIm5iZiI6MTc1MDM0NjU0NS44NDE5OTk4LCJzdWIiOiI2ODU0MmIzMWMwYWRlNmExNjQyOWUyMDciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.SOm_S_Cb__c0YqLJSbpD6jGvxTGMt8JtiYqcKPg0UTs"

def get_all_movies(request):
    return JsonResponse({
        "success": True,
        "movies": [
            {
                "id": movie.id,
                "title": movie.title
            }
            for movie
            in movies[["id", "title"]].itertuples()
        ],
    })

def get_movie_index(movie_title):
    return movies[movies["title"] == movie_title].index[0]

def fetch_movie_details(id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{id}?language=en-US",
        headers={
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    )
    data = response.json()
    print(data)
    if response.status_code == 200: return data
    else: return None

def recommend(request, title):

    # get target movie index
    try: target_movie_index = get_movie_index(title)
    except: return JsonResponse({
        "success": False,
        "error": "movie not found",
        "requested_title": title,
    })

    # get similar movies
    n = 5
    similar_movies = sorted(
        list(enumerate(similarity[target_movie_index])),
        reverse=True,
        key=lambda x:x[1]
    )[1:n+1]

    # structre the similar movie
    recommended_movies = []
    for movie in similar_movies:
        movie_details = fetch_movie_details(int(movies.iloc[movie[0]]["id"]))
        recommended_movies.append({
            "title": movies.iloc[movie[0]]["title"],
            "poster_path": None if movie_details is None else f"https://image.tmdb.org/t/p/w500{movie_details["poster_path"]}",
            "homepage":None if movie_details is None else movie_details["homepage"],
        })

    # return the json response
    return JsonResponse({
        "success": True,
        "requested_title": title,
        "recommended_movies": recommended_movies,
    })
