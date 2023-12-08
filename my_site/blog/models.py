from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import FileExtensionValidator

USER_MODEL = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='chto.png', upload_to='profile_pics')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})