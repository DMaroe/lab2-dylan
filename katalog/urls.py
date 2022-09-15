# TODO: Implement Routings Here
from django.urls import path
from katalog.views import querying

app_name = 'wishlist'

urlpatterns = [
    path('', querying, name='querying'),
]