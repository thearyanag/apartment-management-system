from django.db import models

# Create your models here.
class Flat(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    wing = models.CharField(max_length=100)
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.number

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    departed_at = models.DateTimeField()
    remarks = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return self.name