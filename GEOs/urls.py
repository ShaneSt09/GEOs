from django.urls import path
from . import views  
from GEO_dm import settings
from django.conf.urls.static import static
urlpatterns =[
path("",views.Import_Excel_Pandas,name="Import_Excel_Pandas"),
path('Import_Excel_Pandas/', views.Import_Excel_Pandas,name="Import_Excel_Pandas")
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
