from django.db import models

# Create your models here
class User(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    username = models.CharField(max_length=16, db_column='username')
    email = models.CharField(max_length=255, db_column='email')
    password = models.CharField(max_length=32, db_column='password')
    name = models.CharField(max_length=45, db_column='first_name')

    class Meta:
        managed = False
        db_table = 'auth_user'

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=45)
    cuerpo = models.TextField(default="")
    imagen_url = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='noticias', blank=True)

class NoticiaUsers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    noticia_id = models.ForeignKey(Noticia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_noticia_users'

class TipoBodega(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    metros = models.IntegerField()
    quimicos = models.IntegerField()
    organicos = models.IntegerField()
    hermetico = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.tipo

class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    tipo_bodega = models.ForeignKey(TipoBodega, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.codigo