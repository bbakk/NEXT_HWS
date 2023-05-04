from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(help_text="User Age", blank=True, null=True)

    class Meta:
        verbose_name = "User_Profile"
        verbose_name_plural = "User_Profiles"

    def __str__(self):
        return f'{self.pk}. {self.user}'