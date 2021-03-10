from django.urls import path
from .views import worker

urlpatterns = [
    path('worker/', worker, name="workers")
]