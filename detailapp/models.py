from django.db import models


class UserDetails(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    contact_number=models.IntegerField()
    password = models.IntegerField()

    def __str__(self):
        return self.first_name