from django.db import models

# Create your models here.


class Controller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)
    a = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    custom1 = models.JSONField(default=None, blank=True, null=True)
    custom2 = models.JSONField(default=None, blank=True, null=True)
    custom3 = models.JSONField(default=None, blank=True, null=True)
    custom4 = models.JSONField(default=None, blank=True, null=True)
    custom5 = models.JSONField(default=None, blank=True, null=True)

    def __str__(self: 'Controller') -> str:
        return self.name

    def __repr__(self: 'Controller') -> str:
        return self.name