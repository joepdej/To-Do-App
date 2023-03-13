from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Taak(models.Model):
    gebruiker = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    titel = models.CharField(max_length=200)
    beschrijving = models.TextField(blank=True)
    compleet = models.BooleanField(default=False)
    datumAangemaakt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

    class Meta:
        ordering = ["compleet"]
