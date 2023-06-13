
from PIL import Image
from django.conf import settings
from django.db import models


class Photo(models.Model):
    IMAGE_MAX_SIZE = (800, 800)
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
   

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    contributors = models.ManyToManyField(
    settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')

class Meta:
        permissions = [
            ('change_blog_title', 'Peut changer le titre d’un billet de blog')
        ]
class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)
    
    class Meta:
        unique_together = ('contributor', 'blog')