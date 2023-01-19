from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('communitytype/', views.getCommunityType),
    path('postcommunitytype/', views.postCommunityType),

    path('parish/', views.getParish),
    path('postparish/', views.postParish),

    path('community/', views.getCommunity),
    path('postcommunity/', views.postCommunity),
]