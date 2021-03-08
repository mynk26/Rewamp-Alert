from django.db import models
from account.models import useraccount
from django.utils import timezone
import datetime

# Create your models here.
class tasks(models.Model):
    user = models.ForeignKey(useraccount, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    RevisionDate = models.DateField(default=timezone.now() + timezone.timedelta(days=2))
    TotalRevision = models.IntegerField(default=0)
    marked = models.BooleanField(default=False)
    topic = models.TextField()
    desc = models.TextField()

