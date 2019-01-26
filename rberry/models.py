from django.db import models


class TempHumidity(models.Model):
    temp = models.FloatField()
    humidity = models.FloatField()

    c_on = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        ordering = ["-c_on"]
