from django.db import connection
from django.db.models import Count, Case, When, IntegerField
from .models import *
 
def getNoticiasLikesByUser(user_id):
    return Noticia.objects.annotate(like=Count(Case(When(users__id=user_id, then=1), output_field=IntegerField(),))).annotate(likes=Count('users'))

def addLike(user_id, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.users.add(User.objects.get(id=user_id))
    noticia.save()
    
def removeLike(user_id, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.users.remove(User.objects.get(id=user_id))
    noticia.save()
    