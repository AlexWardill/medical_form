from django.db import models

class Response(models.Model):
    # unsure if these are suitable field types and max_lengths
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)


    def __str__(self):
        return self.name
