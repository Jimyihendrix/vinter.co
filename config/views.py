from django.shortcuts import render # <-??

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Generated token 87002834fb789b780b6e2b254bbb3e80b8bc64d8 for user jimyihendrix

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Vinter Capital'}
        return Response(content)


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>vinter.co - Vinter Capital, building the free economy</h1>")