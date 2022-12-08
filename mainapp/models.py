from django.db import models



from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    email = models.EmailField(max_length=254)
    dob = models.DateTimeField(null=True)



class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_price = models.DecimalField(max_digits = 5,decimal_places = 2)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    bid_end = models.DateField()


class Bids(models.Model):
    name_of_user = models.CharField(max_length=200)
    bid_amount = models.DecimalField(max_digits = 5,decimal_places = 2)


class QandA(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    

