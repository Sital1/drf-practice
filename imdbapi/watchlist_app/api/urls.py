from django.urls import path,include
from watchlist_app.api.views import MovieDetailAV, MovieListAV

#from watchlist_app.api.views import movie_list, movie_details


## Function based views url
# urlpatterns = [
#     path('', movie_list, name='movie-list'),
#     path('<int:pk>', movie_details, name='movie-detail'),
# ]

urlpatterns = [
    path('', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]

