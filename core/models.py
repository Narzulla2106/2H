from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    vaqt = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255)
    davomiylik = models.TextField()
    turi1 = models.CharField(max_length=255)
    turi2 = models.CharField(max_length=255)

    def __str__(self) -> str :
        return self.nomi


