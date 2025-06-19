from django.http import JsonResponse
import pickle, os, pandas as pd

movies_dict_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies_dict.pkl')
similarity_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'similarity.pkl')
with open(movies_dict_path, 'rb') as file: movies_dict = pickle.load(file)
with open(similarity_path, 'rb') as file: similarity = pickle.load(file)
movies = pd.DataFrame(movies_dict)

def get_all_movies(request):
    return JsonResponse({
        "success": True,
        "movies": [{i: title} for i, title in enumerate(movies["title"].values)]
    })

def get_movie_index(movie_title):
    return movies[movies["title"] == movie_title].index[0]

def recommend(request, title):
    try: target_movie_index = get_movie_index(title)
    except: return JsonResponse({
        "success": False,
        "error": "movie not found"
    })
    n = 5
    movie_objs = sorted(
        list(enumerate(similarity[target_movie_index])),
        reverse=True,
        key=lambda x:x[1]
    )[1:n+1]
    return JsonResponse({
        "success": True,
        "requested_title": title,
        "recommended_movies": [movies["title"][x[0]] for x in movie_objs]
    })
