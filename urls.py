from django.urls import path

from django.contrib.sitemaps.views import sitemap
from . import sitemaps

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.document, name="document"),
    path('category/<int:category_id>/', views.collections, name="collection"),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': {
            'Posts': sitemaps.PostSitemap,
            'Categories': sitemaps.CategorySitemap
        }},
        name='django.contrib.sitemaps.views.sitemap')
]
