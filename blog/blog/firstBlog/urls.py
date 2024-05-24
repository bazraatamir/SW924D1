from django.urls import path
from .views import BlogListView, CreateBlog, deleteBlog,UpdateBlog, GetOneBlog 
urlpatterns = [
    path('',BlogListView.as_view()),
    path("create",CreateBlog.as_view()),
    path('delete/<int:pk>/',deleteBlog.as_view()),
    path('update/<int:pk>/',UpdateBlog.as_view()),
    path('getOneBlog/<int:pk>/', GetOneBlog.as_view())
]

