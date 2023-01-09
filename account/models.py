from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import BigAutoField
from datetime import datetime 
from django.db.models.signals import post_save
from django.dispatch import receiver  


# Create your models here.


class User(AbstractUser):
    # id= models.AutoField(primary_key=True, default=True)
    name= models.CharField(max_length=250,null=False,blank=True)
    updated_on = models.DateTimeField(default=datetime.now, blank=True)
    is_excom= models.BooleanField('Is Excom', default=False)
    is_director = models.BooleanField('Is Director', default=False)
    is_member = models.BooleanField('Is Member', default=False)


# class register_table(models.Model):
#     id = models.AutoField(primary_key=True, default=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     name= models.CharField(max_length=250,null=False,blank=True)
#     contact_number = models.CharField(max_length=250,null=True,blank=True)
#     profile_pic =models.ImageField(default='profile.webp', upload_to = "profiles",null=True,blank=True)
#     email = models.EmailField(max_length=250,null=False,blank=True)
#     department = models.CharField(max_length=250,null=True,blank=True)

#     def __str__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         register_table.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Domain(models.Model):
    domain = models.CharField(max_length=80)

    def __str__(self):
        return (self.domain)

class Members(models.Model):
    id= models.AutoField(primary_key=True, default=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    department = models.CharField(max_length=250,null=True,blank=True)
    year = models.CharField(max_length=250,null=True,blank=True)
    contact_number = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=250,null=False,blank=True)
    updated_on = models.DateTimeField(User, default=datetime.now, blank=True)








    


