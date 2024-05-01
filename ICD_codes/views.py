# utils.py
from .models import MainCode, SubCode
from .code_mapping import main
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ImportDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        main()
        return Response("Hello World")