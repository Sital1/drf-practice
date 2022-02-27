from dataclasses import fields
from pyexpat import model
from django.forms import ValidationError
from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Reviews




class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        # fields = '__all__'
        exclude = ('watchlist',)
    
    

# Which model are we using
# What type of fields do we need
# Can also exclude which we don't need

class WatchListSerializer(serializers.ModelSerializer):

    # extra fields
    # Can define method that calculates the length of name
    # len_name = serializers.SerializerMethodField()
    
    # Nested serializer with review
    reviews = ReviewSerializer(many=True, read_only= True)
    
    class Meta:
        model = WatchList
        # Can specify the fields in an array
        fields = '__all__'
        #Exclude exclude = ['name']



class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # create a nested relationships
    # use the name defined in related_name
    # watchlist = WatchListSerializer(many=True, read_only=True)
    
    ## Send only a part of nested use relation filed
    watchlist = serializers.StringRelatedField(many=True, read_only=True)
    
    
    # Add hyperlink for the object
    # need view name
    # For the ID filed used HyperLinkIdentity field
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only=True,
    #     view_name='movie-detail' )
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'

       # fields fields = ['id', 'name', 'description']       

    # # Serializer Method field
    # def get_len_name(self,object):
    #     length = len(object.name)
    #     return length
        
    
    # '''
    #     Validators still required
    # '''
    
    # # Field level validations
    # # value = value of the name field
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    # # Object level validation
    # # data = the whole object
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError(
    #             "Title and description should be different")
    #     return data

    # validator is still required


# ## Function for validator
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# # using serializers Now
# # maps all the values


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     # Validators
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     # takes self and validated data
#     def create(self, validated_data):
#         # create an instance in the database
#         # The data has all the data
#         return Movie.objects.create(**validated_data)

#     # update condition
#     # instance carries old value
#     # validated consist new value
#     def update(self, instance, validated_data):
#         # update each individual value
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get(
#             "description", instance.description)
#         instance.active = validated_data.get("active", instance.active)

#         # save it
#         instance.save()
#         return instance

#     # ## Field level validations
#     # ## value = value of the name field
#     # def validate_name(self,value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value

#     # Object level validation
#     # data = the whole object
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "Title and description should be different")
#         return data
