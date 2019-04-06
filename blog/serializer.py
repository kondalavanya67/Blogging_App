from rest_framework import serializers
from .models import interest, Blog, Comment


class interestSerializer(serializers.ModelSerializer):
    class Meta:
        model = interest
        fields = ('interest_name', 'content', 'base_image', 'related_topics')

    def create(self, validated_data):
        interest_name = validated_data['interest_name']
        content = validated_data['content']
        base_image = validated_data['base_image']
        related_topics = validated_data['related_topics']
        interest1 = interest.objects.create(interest_name=interest_name, content=content, base_image=base_image)
        for each in related_topics:
            interest1.related_topics.add(each)
        return interest1


class bloginterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = interest
        fields = ('interest_name',)


class BlogSerializer(serializers.ModelSerializer):
    interests = bloginterestSerializer()

    class Meta:
        model = Blog
        fields = ('author', 'heading', 'draft', 'content', 'upvotes', 'post_date', 'interests')

    def create(self, validated_data):
        author = validated_data['author']
        heading = validated_data['heading']
        draft = validated_data['draft']
        content = validated_data['content']
        upvotes = validated_data['upvotes']
        # post_date=validated_data['post_date']
        interests = validated_data['interests']
        qs = interest.objects.filter(interest_name=interests['interest_name'])
        print(interests['interest_name'])
        if qs.exists():
            interest_var = interest.objects.get(interest_name=interests['interest_name'])
            Blog1 = Blog.objects.create(author=author, heading=heading, draft=draft, content=content,
                                        interests=interest_var)
            for each in upvotes:
                Blog1.upvotes.add(each)
            Blog1.save()
            return Blog1
