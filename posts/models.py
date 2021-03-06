from django.db import models


class PostRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)


class Posts(models.Model):
    post_title = models.CharField(max_length=24)
    post_body = models.TextField(max_length=1000)
    rates = models.OneToOneField(PostRates, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title