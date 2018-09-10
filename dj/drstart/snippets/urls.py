# -*- coding:UTF-8 -*-

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    #path('', views.snippet_list),
    #path('<int:pk>/', views.snippet_detail),
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)  # 好像失效了？
