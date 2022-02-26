from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchListDetailtAV, StreamListAV, StreamDetailsAv

#from watchlist_app.api.views import movie_list, movie_details


## Function based views url
# urlpatterns = [
#     path('', movie_list, name='movie-list'),
#     path('<int:pk>', movie_details, name='movie-detail'),
# ]

urlpatterns = [
    path('watchlists', WatchListAV.as_view(), name='movie-list'),
    path('watchlists/<int:pk>', WatchListDetailtAV.as_view(), name='movie-detail'),
    path('streamplatformlists', StreamListAV.as_view(), name='platform-list'),
    path('streamplatformlists/<int:pk>', StreamDetailsAv.as_view(), name='platform-detail'),
]

