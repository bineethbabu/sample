from django.db import models

# Create your models here.
class studentdetails(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    contact=models.TextField()
    email=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/", null=True)