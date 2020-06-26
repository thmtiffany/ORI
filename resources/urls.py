from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'resources'),
    path('<int:pk>/', PostDetailView.as_view(), name = 'resources-detail'),
    path('new/', PostCreateView.as_view(), name = 'resources-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name = 'resources-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'resources-delete'),
]