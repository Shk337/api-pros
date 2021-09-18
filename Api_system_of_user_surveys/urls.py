from django.contrib import admin
from django.urls import path, include


     ###############     Добавить путь  api ############

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('api/', include('surveysApp.urls')),
]

