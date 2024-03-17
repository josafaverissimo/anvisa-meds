from django.urls import path
from .views import PmvgDataInsertView, MedsView

urlpatterns = [
    path('resources/pmvg-data/insert/', PmvgDataInsertView.as_view()),
    path('meds/', MedsView.as_view())
]
