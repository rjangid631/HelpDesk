from django.db import models

class Priority(models.Model):
    PriorityID = models.IntegerField(primary_key=True)
    PriorityName = models.CharField(max_length=50)

    def __str__(self):
        return self.PriorityName