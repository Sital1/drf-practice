from asyncio import mixins
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamPlatform, Reviews


'''
    Generic views
    Generic Api view at at last
    Import all the mixin
'''

class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    
    # queryset.. gets the object
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

'''
 APi views
'''
class WatchListAV(APIView):
    # no need to use if condition. directly define method

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # data is from the return in the create method in the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class WatchListDetailtAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        # Put means update every single field. Rewrite everything.
        # Someone is sending the data
        # which object are we updating?
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # fetch the data
        movie = WatchList.objects.get(pk=pk)
        # delete it. is a queryset method
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamListAV(APIView):

    def get(self, request):
        streamPlatform = StreamPlatform.objects.all()
        ## need context when using HyperlinkRelation
        #serializer = StreamPlatformSerializer(streamPlatform, many=True, context={'request': request})
        serializer = StreamPlatformSerializer(streamPlatform, many=True)
        return Response(serializer.data)
    
    def post(selr,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class StreamDetailsAv(APIView):
    
    def get(self,request,pk):
        
        ## get the platform according to the pk in a try clatch block
        try:
            streamPlatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Streamplatform not found'}, status=status.HTTP_404_NOT_FOUND)
        ## return the platform 
        serializer = StreamPlatformSerializer(streamPlatform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(streamPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # fetch the data
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        # delete it. is a queryset method
        streamPlatform.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






'''
Functional views
'''

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':

#         # get all the data first
#         movies = Movie.objects.all()

#         # utilize serializer.
#         # Serializer needs to visit Multiple objects. So many=true
#         serializer = WatchListSerializer(movies, many=True)

#         # Send the data. Serializer is an object. Use .data to access the object
#         return Response(serializer.data)

#     # Get data from user
#     if request.method == 'POST':
#         # request will have the data

#             serializer = WatchListSerializer(data=request.data)


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
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         # Put means update every single field. Rewrite everything.
#         # Someone is sending the data
#         # which object are we updating?
#         movie = Movie.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie,data=request.data)
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
