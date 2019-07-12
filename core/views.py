from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework import generics
from core.models import TestModel
from core.serializers import TestModelSerializer
from django.http import Http404


# from django.contrib.auth.models import User
# from core.serializers import UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {'message': 'Yo ppl'}
        return Response(content)


class TestModelList(APIView):

    def get(self, request, format=None):
        users = TestModel.objects.all()
        serializer = TestModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class TestModelPerson(APIView):

    def get_object(self, user_id):
        try:
            return TestModel.objects.get(id=user_id)
        except TestModel.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        user = self.get_object(user_id)
        serializer = TestModelSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        user = self.get_object(user_id)
        serializer = TestModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
