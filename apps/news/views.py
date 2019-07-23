from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import NewsModelSerializer, NewsModel


class NewsModelSingle(APIView):

    def get_object(self, news_id):
        try:
            return NewsModel.objects.get(news_id=news_id)
        except NewsModel.DoesNotExist:
            raise Http404

    def get(self, request, news_id, format=None):
        user = self.get_object(news_id)
        serializer = NewsModelSerializer(user)
        return Response(serializer.data)

    def put(self, request, news_id, format=None):
        user = self.get_object(news_id)
        serializer = NewsModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, news_id, format=None):
        snippet = self.get_object(news_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsModelList(APIView):

    def get(self, request, format=None):
        news = NewsModel.objects.all()
        serializer = NewsModelSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
