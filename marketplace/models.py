from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):

    def __str__(self):
        return self.product_name

    product_id = models.IntegerField(unique=True)
    product_category = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_image = models.CharField(max_length=800,default="https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png")
    product_stock = models.BooleanField()
    product_price = models.FloatField()
    sale_price = models.FloatField()
    description = models.TextField(null=True)
    modified_date = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)


class Friends(models.Model):

    user_id = models.IntegerField()
    friends_list = models.TextField()

class product_views(models.Model):

    user_id = models.IntegerField()
    views_list = models.TextField()
