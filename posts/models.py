from django.db import models


class Post(models.Model):                                           #inheritance
    title = models.CharField(max_length=128)                        #composition
    subtitle = models.CharField(max_length=256)                     #composition
    body = models.TextField()                                       #composition
    created_on = models.DateTimeField(auto_now_add=True)            #composition
