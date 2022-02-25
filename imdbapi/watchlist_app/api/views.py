from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        
        # get all the data first
        movies = Movie.objects.all()
        
        # utilize serializer. 
        # Serializer needs to visit Multiple objects. So many=true
        serializer = MovieSerializer(movies, many=True)
        
        # Send the data. Serializer is an object. Use .data to access the object
        return Response(serializer.data)
    
    # Get data from user
    if request.method == 'POST':
        # request will have the data
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # data is from the return in the create method in the serializer
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        # Put means update every single field. Rewrite everything.
        # Someone is sending the data
        # which object are we updating?
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        # fetch the data
        movie = Movie.objects.get(pk=pk)
        # delete it. is a queryset method
        movie.delete()
        
        return Response()