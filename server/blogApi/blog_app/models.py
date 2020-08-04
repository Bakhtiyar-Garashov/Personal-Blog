from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique=True,
                            null=True, blank=True, editable=False)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
