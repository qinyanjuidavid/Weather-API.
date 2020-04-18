from django.db import models



class Place(models.Model):
    city=models.CharField(max_length=200,unique=True)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.city
