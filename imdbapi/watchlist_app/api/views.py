from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


class MovieListAV(APIView):
    # no need to use if condition. directly define method

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # data is from the return in the create method in the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        # Put means update every single field. Rewrite everything.
        # Someone is sending the data
        # which object are we updating?
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # fetch the data
        movie = Movie.objects.get(pk=pk)
        # delete it. is a queryset method
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':

#         # get all the data first
#         movies = Movie.objects.all()

#         # utilize serializer.
#         # Serializer needs to visit Multiple objects. So many=true
#         serializer = MovieSerializer(movies, many=True)

#         # Send the data. Serializer is an object. Use .data to access the object
#         return Response(serializer.data)

#     # Get data from user
#     if request.method == 'POST':
#         # request will have the data

#             serializer = MovieSerializer(data=request.data)


#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED) # data is from the return in the create method in the serializer
#             else:
#                 return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         # Put means update every single field. Rewrite everything.
#         # Someone is sending the data
#         # which object are we updating?
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         # fetch the data
#         movie = Movie.objects.get(pk=pk)
#         # delete it. is a queryset method
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
