from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageModel(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name = "messages")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
# Create your models here.
