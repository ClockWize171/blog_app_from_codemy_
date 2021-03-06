from django.urls import path,include
#from . import views
from .views import HomeView, DetailView, PostView, UpdatePost, DeletePost, CategoryView, CategoryPageView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="article_detail"),
    path('add-post/', PostView.as_view(), name="add_post"),
    path('add-category/', CategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryPageView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),

]