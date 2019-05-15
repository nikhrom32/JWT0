from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Yo ppl'}
        return Response(content)
