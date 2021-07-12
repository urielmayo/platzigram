from django.db import models
from django.contrib.auth.models import User

from users.models import Profile
# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE
    )
    
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    liked = models.ManyToManyField('users.Profile', related_name='liked_by')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @ {self.user}'

#para avisar a django que hicimos cambios en la base de datos:
#   python3 manage.py makemigrations

#para realizar los cambios hechos:
#   python3 manage.py migrate