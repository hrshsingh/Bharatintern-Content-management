from django.db import models

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=30)
    content=models.TextField()
    author=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

