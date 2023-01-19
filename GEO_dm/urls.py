from django.contrib import admin
from django.urls import path,include

admin.site.site_header  =  "GEOS"
admin.site.index_title = "GEOS"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('geos.urls')),
]
