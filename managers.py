from django.db import models


class PostManager(models.Manager):

    def year(self, year):
        return super(PostManager, self).get_queryset().filter(created_at__year=year)

    def month(self, year, month):
        return super(PostManager, self).get_queryset().filter(created_at__year=year, created_at__month=month)

    def tag(self, slug):
        return super(PostManager, self).get_queryset().filter(tags__slug=slug)

    def category(self, slug):
        return super(PostManager, self).get_queryset().filter(category__slug=slug)

    def user(self, username):
        return super(PostManager, self).get_queryset().filter(author__username=username)

    def slug(self, slug):
        return super(PostManager, self).get(slug=slug)