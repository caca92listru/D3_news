from django.urls import path
from .views import PostList, PostDetailView,   PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('news_search/', PostSearch.as_view(), name='news_search'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail')
]