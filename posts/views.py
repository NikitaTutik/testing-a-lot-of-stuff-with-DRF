from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Posts, PostRates
from .serializers import PostsSerializer, PostRatesSerializer


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostsSerializer

    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data
        new_rate = PostRates.objects.create(likes=post_data['rates']['likes'], dislikes=post_data['rates']['dislikes'])
        new_rate.save()

        new_post = Posts.objects.create(post_title=post_data['post_title'], post_body=post_data['post_body'],
                                        rates=new_rate)
        new_post.save()
        serializer = PostsSerializer(new_post)
        return Response(serializer.data)


class PostRatesViewset(viewsets.ModelViewSet):
    serializer_class = PostRatesSerializer

    def get_queryset(self):
        rates = PostRates.objects.all()
        return rates

