# Django import 
from django.db import models

class Translation(models.Model):
    text = models.TextField()
    target_language = models.CharField(max_length=10)
    source_language = models.CharField(max_length=10, default='auto')
    translated_text = models.TextField()

    def __str__(self):
        return f'Translation: {self.text} ({self.source_language} -> {self.target_language})'

