from django.urls import path

from .views import PostListView, PostDetailView

# app_name = "blog_app"

urlpatterns = [
    path("posts", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
