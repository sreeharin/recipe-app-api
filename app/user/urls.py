from django.urls import path
from .views import CreateUserApiView


app_name = 'user'
urlpatterns = [
    path('create/', view=CreateUserApiView.as_view(), name='create'),
]