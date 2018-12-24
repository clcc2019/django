from django.db import models
class HostName(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.URLField()
    ctime = models.DateField()
    ssl_time = models.DateField()
    ssl_otime = models.DateField()
    ssl = models.FileField(upload_to='ssl_up',null=True,blank=True)
    def __str__(self):
        return self.name
