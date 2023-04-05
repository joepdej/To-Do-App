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
    datumKlaar = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.titel

    class Meta:
        ordering = ["compleet"]



class Invitation(models.Model):
    sender = models.ForeignKey(User, related_name='sent_invitations', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_invitations', on_delete=models.CASCADE)
    task_list = models.ForeignKey(Taak, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} invited {self.recipient.username} to {self.task_list.titel}"
