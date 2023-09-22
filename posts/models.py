from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField( max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)
    # MANY USER CAN LIKE 1 POST AND 1 USER CAN LIKE MANY POSTS
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='posts_liked')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# CREATE COMMENT MODEL
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    body = models.CharField(max_length=200)
    created = models.DateField(auto_now=True)
    comment_by = models.CharField(max_length=100, default='Anonymous')

    class Meta:
        # WHENEVER LOOP OVER COMMENTS ORDER BY CREATED DATE
        ordering = ('created',)

    def __str__(self):
        return self.body 
    
