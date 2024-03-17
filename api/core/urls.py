from django.urls import path
from .views import PmvgDataInsertView

urlpatterns = [
    path('resources/pmvg-data/insert/', PmvgDataInsertView.as_view())
]
