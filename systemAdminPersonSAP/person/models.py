from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    number_street = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Address {self.id}: {self.street} {self.number_street} {self.country}'

    # python manage.py makemigrations
    # python manage.py migrate


class Person(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True) # SET_NULL -> it is if we delete a raw

    def __str__(self):
        return f'Person {self.id}: {self.name} {self.lastname} {self.email}'
        # that is to see correctly in the admin page all raws






