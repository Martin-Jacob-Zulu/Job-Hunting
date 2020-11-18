from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models.signals import pre_save, post_delete, post_save
# from django.utils.text import slugify
from django.dispatch import receiver


class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    TECHNICAL = 'technical'
    DESIGN = 'design'
    CULTURE = 'culture'
    POLITICS = 'politics'
    BUSINESS = 'business'
    WORK = 'work'
    SCIENCE = 'science'
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel'


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.BUSINESS)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    excerpt = models.CharField(max_length=150)
    uploaded = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while queryset:
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
