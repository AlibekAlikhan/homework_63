from django.urls import path

from accounts.views import logout_view
from posts.views import PostsView, PostsCreateView, PostsProfileView, CommentDetailView, LikeView

urlpatterns =[
    path('', PostsView.as_view(), name='index'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name="to_comment"),
    path('post/create', PostsCreateView.as_view(), name='post_create'),
    path('logout/', logout_view, name='logout'),
    path('like/<int:pk>', LikeView.as_view(), name='like'),
]