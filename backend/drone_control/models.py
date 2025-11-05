from django.db import models 
class Drone(models.Model): 
    name = models.CharField(max_length=100) 
    status = models.CharField(max_length=20, default='IDLE') 
