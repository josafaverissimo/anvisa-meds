from django.urls import path
from .views import MedsPriceView

urlpatterns = [
    path('', MedsPriceView.as_view())
]
