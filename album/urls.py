from django.contrib import admin
from django.urls import path, include
from album import views

urlpatterns = [
    path('', views.base, name="base"),
   #path('', views.Main, name='base1.html'),
    path( '', views.first_view, name="first view"),
    path('category/', views.CategoryListView.as_view(), name='category-list'),      
    #path('category/',views.category, name='category'),

    
    path('category/<int:category_id>/detail/', views.category_detail, name='category-detail'),
    
    
    #path('category/', views.CategoryListView.as_view(), name='category-detail'),
    path('photo/', views.Photo, name='photo-list'),
    #path('photo/', views.PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>/detail/', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/<int:pk>/update', views.PhotoUpdate.as_view(), name='photo-update'),
    path('photo/create', views.PhotoCreate.as_view(), name='photo-create'),
    path('photo/<int:pk>/delete', views.PhotoDelete.as_view(), name='photo-delete'),
]