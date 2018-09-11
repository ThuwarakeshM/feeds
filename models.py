from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.sitemaps import ping_google


class Category(models.Model):
    category = models.CharField(max_length=20)
    category_en = models.CharField(max_length=20)
    category_image = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=now())

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return '/category/{}/'.format(self.id)

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass




class Post(models.Model):
    page_title = models.CharField(max_length=60)
    page_desc = models.CharField(max_length=160)
    page_keywords = models.CharField(max_length=100)

    title = models.CharField(max_length=300)
    desc = models.TextField(blank=True)
    img = models.CharField(max_length=300, blank=True)
    img_alt = models.CharField(max_length=100, blank=True)
    vid = models.CharField(max_length=300, blank=True)
    pub_date = models.DateTimeField(default=now())

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/{}/'.format(self.id)

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass


class Section(models.Model):
    title = models.CharField(max_length=300, blank=True)
    desc = models.TextField(blank=True)
    img = models.CharField(max_length=300, blank=True)
    img_alt = models.CharField(max_length=100, blank=True)
    vid = models.CharField(max_length=300, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


