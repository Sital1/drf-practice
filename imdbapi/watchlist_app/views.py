# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.


# def movie_list(request):
#     # Create a queryset
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}

#     return JsonResponse(data)
#     # return in the form of JSON


# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {'movie': movie.name, 'movie_id': movie.id,
#             'movie_description': movie.description, 'active': movie.active}

#     return JsonResponse(data)
