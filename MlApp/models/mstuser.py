from django.db import models

# Create your models here.
class Mst_user(models.Model):
    """
    Mstuser to do.
    """
    id = models.CharField(primary_key=True,max_length=5)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mailaddress = models.CharField(max_length=40)
    adminflg = models.CharField(max_length=1)
    createdate = models.DateTimeField()
    updatedate = models.DateTimeField()
