from django.db import models

# Create your models here.


class NeedyPerson(models.Model):
    
    phoneOfNeedy = models.IntegerField()
    messageOfNeedy = models.TextField(max_length = 80)
    photoOfNeedy = models.ImageField(upload_to = 'photoUploads/')
    audioOfNeedy = models.FileField(upload_to='musics/')
    
    def __str__(self):
        return "This is " + str(self.phoneOfNeedy)
    
class HelpModel(models.Model):
    phoneOfNeedy = models.IntegerField()
    message = models.TextField(max_length = 200)
    
    def __str__(self):
        return "Query message from " + str(self.phoneOfNeedy)