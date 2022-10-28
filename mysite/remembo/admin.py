from django.contrib import admin

# Register your models here.
from .models import deck, flashcard
admin.site.register(deck)
admin.site.register(flashcard)