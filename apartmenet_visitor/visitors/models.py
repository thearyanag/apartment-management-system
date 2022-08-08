from django.db import models
from django.utils.html import mark_safe
import datetime

# Create your models here.
class Flat(models.Model):
    flat_number = models.IntegerField()
    name = models.CharField(max_length=100)
    members = models.CharField(max_length=100, blank=True, null=True)
    vehicle_number = models.CharField(max_length=100, blank=True, null=True)
    wing = models.CharField(max_length=100)
    floor = models.IntegerField()
    number = models.CharField(max_length=100)

    def __str__(self):
        return str(self.flat_number) + " " + self.name

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    address = models.CharField(max_length=100 , blank=True)
    flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    departed_at = models.DateTimeField(blank=True)
    remarks = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return self.name + " Flat= " + str(self.flat)

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServicePerson(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    phone = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    vehicle_number = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(ServiceType, on_delete=models.PROTECT)
    flat = models.ManyToManyField(Flat)

    def image_tag(self):
            return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    fields = ['image_tag']
    readonly_fields = ['image_tag']

    def __str__(self):
        return self.name + " " +str(self.type)

class ServiceRegister(models.Model):
    name = models.ForeignKey(ServicePerson, on_delete=models.PROTECT)
    flat = models.ForeignKey(Flat, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    departed_at = models.DateTimeField()
    remarks = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return str(self.name) + " Flat= " + str(self.flat)
