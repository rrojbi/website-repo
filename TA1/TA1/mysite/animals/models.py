from django.db import models

class Animal(models.Model):
    id_animal = models.CharField(max_length=200)
    Etat = models.CharField(max_length=200)
    Lieu = models.CharField(max_length=200)
    def __str__(self):
       return (self.id_animal)

class Action(models.Model):
    Action_text = models.CharField(max_length=200)
    def __str__(self):
        return self.Action_text
