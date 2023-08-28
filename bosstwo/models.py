from django.db import models
import uuid

class StaffTwo(models.Model):
    id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    qualification = models.CharField(max_length=60)
    level = models.IntegerField()
    dateadded = models.DateTimeField(auto_now_add=True)

