from rest_framework import generics
from .models import BlogModel
from .Serializer import BlogSerializer

# Create your views here.

class BlogListView(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class CreateBlog(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class deleteBlog(generics.DestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class UpdateBlog(generics.UpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class GetOneBlog(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer