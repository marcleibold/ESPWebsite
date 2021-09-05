from django.db import models

# Create your models here.


class Controller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rgb = models.JSONField(default=None, blank=True, null=True)
    brightness = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    custom1 = models.JSONField(default=None, blank=True, null=True)
    custom2 = models.JSONField(default=None, blank=True, null=True)
    custom3 = models.JSONField(default=None, blank=True, null=True)
    custom4 = models.JSONField(default=None, blank=True, null=True)
    custom5 = models.JSONField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
