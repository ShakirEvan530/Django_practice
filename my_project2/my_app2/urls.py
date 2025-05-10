from django.urls import path
from my_app2.views import learning_django,learning_api
# from my_app2.views import learning_api
urlpatterns = [
    path('dj/',learning_django),
    path('lapi/',learning_api),
]