from unicodedata import name
from django.db import router
from rest_framework.routers import DefaultRouter

from django.urls import path, include
from watchlist_app.api.views import (
    WatchListAV, WatchListDetailtAV, StreamPlatformVS, ReviewList, ReviewDetail,ReviewCreate)

#from watchlist_app.api.views import movie_list, movie_details


# Function based views url
# urlpatterns = [
#     path('', movie_list, name='movie-list'),
#     path('<int:pk>', movie_details, name='movie-detail'),
# ]

router = DefaultRouter()

## register the url
router.register('stream', StreamPlatformVS, basename='stream-platform')

urlpatterns = [
    path('watchlists', WatchListAV.as_view(), name='movie-list'),
    path('watchlists/<int:pk>', WatchListDetailtAV.as_view(), name='movie-detail'),
    
    # include the viewset routers
    path('', include(router.urls)),

    
    # path('streamplatformlists', StreamListAV.as_view(), name='platform-list'),
    # path('streamplatformlists/<int:pk>',
    #      StreamDetailsAv.as_view(), name='platform-detail'),
    # path('reviews', ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    
    
     path('watchlists/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
     path('watchlists/<int:pk>/review', ReviewList.as_view(), name='review-list'),
     path('watchlists/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
]
