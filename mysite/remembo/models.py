from django.db import models

# Create your models here.

class deck(models.Model):
    deck_name = models.CharField(max_length=100)
    deck_bookmark = models.CharField(max_length=20, default="")
    def __str__ (self):
        return self.deck_name

class flashcard(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    deck_key = models.ForeignKey(deck, on_delete=models.CASCADE)
    def __str__ (self):
        return self.front
    def __str__ (self):
        return self.back
