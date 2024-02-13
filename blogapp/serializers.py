from rest_framework import serializers
from blogapp.models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=blogAdd
        fields=(
            'userid',
            'title',
            'message'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields=(
            
            'name',
            'profile',
            'email',
             'password'
        )