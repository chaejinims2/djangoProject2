from django.urls import path

from likeapp.views import LikeArticleView

urlpatterns = [
    path('article/<int:article_pk>', LikeArticleView.as_view(), name='article_like'),
]