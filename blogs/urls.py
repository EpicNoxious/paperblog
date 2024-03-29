from django.urls import path
from . import views
from .views import IndexView, BlogsView, BlogView, AddBlogView, UpdateBlogView, DeleteBlogView, LikeView
urlpatterns = [
  path('', IndexView.as_view(), name="index"),
  
  path('blogs/', BlogsView.as_view(), name="blogs"),
  path('blogs/<uuid:pk>/', BlogView.as_view(), name="blog"),
  
  # path('signin/', views.userSignIn, name="signin"),
  # path('signup/', views.userSignUp, name="signup"),
  
  path('blogs/add/', AddBlogView.as_view(), name="add"),
  path('blogs/update/<uuid:pk>/', UpdateBlogView.as_view(), name="update"),
  path('blogs/delete/<uuid:pk>/', DeleteBlogView.as_view(), name="delete"),
  
  path('like/<uuid:pk>', LikeView , name="like_post"),
  ]
 