from django.db import models

# Create your models here.
class crud(models.Model):
    sl_no=models.IntegerField()
    item_name=models.CharField(max_length=20)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.item_name