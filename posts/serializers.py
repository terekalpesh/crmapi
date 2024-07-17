from rest_framework import serializers
from .models import Post, Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'summary',
            'document',
            'categories',
            'author',
        )

        def validate_document(self, value):
            if not value.name.endswith('.pdf'):
                raise serializers.ValidationError('Only PDF files are allowed.')

    

    
    
       

