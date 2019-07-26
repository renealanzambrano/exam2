from django.db import models
from django.shortcuts import render
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.utils import timezone
# Create your views here.
class Genero(models.Model):
    genero1= models.CharField(max_length=50, null=True)
    created = models.DateTimeField(default = timezone.now);
    delete = models.BooleanField(default=False);

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Genero'
class Ciudad(models.Model):
    city= models.CharField(max_length=50, null=True)
    created = models.DateTimeField(default = timezone.now)
    delete = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Ciudad'

class Estado(models.Model):
    relation = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(default = timezone.now)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Estado'

class Civil(models.Model):
    name= models.CharField(max_length=100, null=False)
    ap_pat= models.CharField(max_length=10,null=False)
    ap_mat= models.CharField(max_length=10,null=False)
    fechaNacimiento= models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=250, null= False)
    telefono= models.IntegerField(null=False)
    genero_pk= models.ForeignKey(Genero,on_delete = models.SET(-1),null=True)
    city_pk= models.ForeignKey(Ciudad,on_delete = models.SET(-1),null=True)
    relation_pk= models.ForeignKey(Estado, on_delete = models.SET(-1),null=True)
    created = models.DateTimeField(default = timezone.now);
    delete = models.BooleanField(default=False);

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Civil'

