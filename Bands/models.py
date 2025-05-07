from django.db import models

class Musicians(models.Model):
    fullNames = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    def __str__(self):
        return f"Musicians(id={self.id}, fullNames={self.fullNames}, telephone={self.telephone})"
    

class Venue(models.Model):
    name=models.CharField(max_length=50)
    def _str_(self):
        return f"Venue(id={self.id}, name={self.name})"
    
class Room(models.Model):
    name= models.CharField(max_length=50)
    venue= models.ForeignKey(Venue, on_delete=models.CASCADE)
    def _str_(self):
        return f"Room(id={self.id}, name={self.name}, venue={self.venue})"
    

class Band(models.Model):
    name= models.CharField(max_length=50)
    musicians= models.ManyToManyField(Musicians)
    def _str_(self):
        return f"Band(id={self.id}, name={self.name})"

