from dataclasses import fields
from pyexpat import model
from django.forms import ValidationError
from rest_framework import serializers

from watchlist_app.models import Movie

# Which model are we using
# What type of fields do we need
# Can also exclude which we don't need


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # Can specify the fields in an array
        fields = '__all__'
        #Exclude exclude = ['name']
        

        # pass list or a tuple for each individual fields
        '''
            fields = ['id', 'name', 'description']       
            
        '''
        
        
        
    
    '''
        Validators still required
    '''
    
    # Field level validations
    # value = value of the name field
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

    # Object level validation
    # data = the whole object
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                "Title and description should be different")
        return data

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
