from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentList,
    CommentCreate,
    SportList,
    SportCreate,
)


urlpatterns = [
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('comment/',
    #      CommentList.as_view(),
    #      name='blog_comment_list_urlpattern'),
    # path('comment/create/',
    #      CommentCreate.as_view(),
    #      name='blog_comment_create_urlpattern'),
    path('sport/',
         SportList.as_view(),
         name='blog_sport_list_urlpattern'),
    path('sport/create/',
         SportCreate.as_view(),
         name='blog_sport_create_urlpattern'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]