from django.db import models


class ExportData(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()

    def __str__(self):
        return f'{self.name}'

