from django.db import models

class Average(models.Model):
    class Meta:
        app_label = 'project'
        db_table = 'example'
    time = models.TextField()
    average_value = models.TextField()