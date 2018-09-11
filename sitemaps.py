from django.contrib.sitemaps import Sitemap
from .models import Post, Category


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date


class CategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
