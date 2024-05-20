from django.urls import path,include
from .views import home ,todoData, UpdateDestroy
from rest_framework.routers import DefaultRouter

urlpatterns =[
    path('',home),
    path('data',todoData.as_view()),
    path('data/<int:id>',UpdateDestroy.as_view())
]   