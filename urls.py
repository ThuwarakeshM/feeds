from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.document, name="document"),
    path('category/<int:category_id>/', views.collections, name="collection"),
]
