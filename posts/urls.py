from django.urls import path
from .views import PostList, PostDetail, CategoryList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_details'),
    path('cat/<int:pk>/', CategoryList.as_view()),
    path('', PostList.as_view(), name='post_list'),
]
