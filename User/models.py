from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_customuser_from_user(user):
    '''
    :param user: Instance from User class
    :return: Corresponding MyUser instance, or None if the
    instance does not exist
    '''
    cUser = None
    cUser_query_set = CustomUser.objects.filter(user=user)
    if len(cUser_query_set) > 0:
        cUser = cUser_query_set.first()
    return cUser

class CustomUser(models.Model):
    ROLES = [
        ('SU', 'superuser'),
        ('CS', 'customer service'),
        ('CU', 'customer'),
        ('BP', 'business partner'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank = True, null = True)
    role = models.CharField(max_length=2,
                            choices=ROLES,
							default='CU',
                            )
