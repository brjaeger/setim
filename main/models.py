import uuid  # tambahkan baris ini di paling atas
from django.db import models

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # mood = models.CharField(max_length=255)
    # time = models.DateField(auto_now_add=True)
    # feelings = models.TextField()
    # mood_intensity = models.IntegerField()

    # @property
    # def is_mood_strong(self):
    #     return self.name
    