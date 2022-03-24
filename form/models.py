from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password= models.CharField(max_length=50)
    
    
    
    def __str__(self):
        # pass this (self) class
        return self.name
        # pass here the key you want its value to be displayed in admin pane (rename record object)
    class Meta:
      verbose_name = "User"
    # name of Table in admin panel can be changed here(rename table)



