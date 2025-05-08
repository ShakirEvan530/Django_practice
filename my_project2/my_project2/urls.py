from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app2/',include('my_app2.urls'))
    
]
