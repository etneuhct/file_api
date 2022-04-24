from django.db import models

# Create your models here.


class StoredFile(models.Model):
    file = models.FileField(upload_to='uploads/')
