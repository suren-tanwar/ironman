
from django.contrib import admin
from django.urls import path ,include
# from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('basic_api.urls'))
    #    url(r'^api/', include('basic_api.urls',)),
]