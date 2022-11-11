from django.urls import path
from . import views

from blogs.views import createPostView, IndexView, PostDetailView, UpdatePostView, delete_Post, search_posts, LikeView

app_name= 'blogs'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('search_posts/', search_posts, name='search-Posts'),
    path('<int:id>/', PostDetailView.as_view(), name='postDetail'),
    path('<int:id>/update_post', UpdatePostView.as_view(), name='postModify'),
    path('<int:id>/delete_post', delete_Post, name='postDelete'),
    path('<int:id>/like', LikeView, name='like_post'),
    # path('<slug:slug>/', post_detail, name='post_detail'),
    path('create_post/', createPostView.as_view(), name='create_post'),
]
# path('index/', index, name='index'),
