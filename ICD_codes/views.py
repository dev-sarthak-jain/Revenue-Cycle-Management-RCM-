from .models import MainCode, SubCode
from .code_mapping import main as Import_main
from .mapping_to_CSV import main as CSV_main
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

'''
class ImportDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        Import_main()
        return Response("Hello World")
    
class ImportDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        CSV_main()
        return Response("Hello")
'''