from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('update_prod/<int:pk>/', views.PostUpdate.as_view()),
    path('create_prod/', views.PostCreate.as_view()),
    path('category/<str:slug>', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('', views.PostList.as_view()),
]