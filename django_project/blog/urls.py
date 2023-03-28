
# 현재 폴더의 views를 사용한다.
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
]