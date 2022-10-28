from django.db import models
from django.contrib.auth.models import User #Django's built-in User model
# Create your models here.
class Item(models.Model):
    #user_name = models.ForeignKey(User, on_delete = models.CASCADE) MUST REDO THIS
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://pluspack.com/wp-content/uploads/2018/09/placeholder-picture.jpg")


    def __str__(self):
        return self.item_name