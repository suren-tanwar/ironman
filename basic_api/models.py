from django.db import models

class DragonMasterModel(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.title
