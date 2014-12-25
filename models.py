from django.db import models
from django.conf import settings
from managers import PostManager
import hashlib


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    category = models.ForeignKey(
        'Category', blank=True, null=True, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    objects = PostManager()

    @property
    def comment_count(self):
        return self.comments.count()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    author_email = models.EmailField(max_length=254)
    author_name = models.CharField(max_length=64, null=True, blank=True)
    author_website = models.URLField(blank=True, null=True)
    content = models.TextField()

    @property
    def gravatar_url(self):
        gravatar_hash = hashlib.md5(self.author_email.lower()).hexdigest()
        return "http://www.gravatar.com/avatar/{}".format(gravatar_hash)

    @property
    def get_author_name(self):
        if self.author_name:
            return self.author_name
        else:
            return 'Anonymous'

    def __unicode__(self):
        return "{} - {}".format(self.get_author_name, self.post.title)

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL)
