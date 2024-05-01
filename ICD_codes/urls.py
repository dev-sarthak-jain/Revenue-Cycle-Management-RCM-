# urls.py
from django.urls import path
from .views import ImportDataAPIView

urlpatterns = [
    path('import-data/', ImportDataAPIView.as_view(), name='api-import-data'),
]
