from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    #Cust_id = models.CharField(max_length=30, primary_key=True)
    Cust_id = models.OneToOneField(User, primary_key=True, unique=True, on_delete=models.CASCADE)
    #Password = models.CharField(max_length=100)
    Name = models.CharField(max_length=50, blank=True, null=True)
    #Email = models.CharField(max_length=30, blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    sexes = models.IntegerChoices("sexes", "Male Female")
    Sex = models.IntegerField(choices=sexes.choices, blank=True, null=True)
    Height = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    Mother_tongue = models.CharField(max_length=20, blank=True, null=True)
    Occupation = models.CharField(max_length=30, blank=True, null=True)
    Income = models.IntegerField(blank=True, null=True)
    City = models.CharField(max_length=20, blank=True, null=True)
    Country = models.CharField(max_length=20, blank=True, null=True)
    Religion = models.CharField(max_length=20, blank=True, null=True)
    drinks = models.IntegerChoices("drinks", "Drink No-Drink")
    Drink = models.IntegerField(choices=drinks.choices, blank=True, null=True)
    smokes = models.IntegerChoices("smokes", "Smoke No-Smoke")
    Smoke = models.IntegerField(choices=smokes.choices, blank=True, null=True)
    diets = models.IntegerChoices("diets", "Veg Non-Veg")
    Diet = models.IntegerField(choices=diets.choices, blank=True, null=True)
    Highest_Education = models.CharField(max_length=20, blank=True, null=True)
    prevms = models.IntegerChoices("prevms", "Married Divorced Unmarried")
    Prev_Marital_Status = models.IntegerField(choices=prevms.choices, blank=True, null=True)
    About_Me = models.CharField(max_length=200, blank=True, null=True)
    matched = models.IntegerChoices("matched", "Matched Unmatched")
    Matched = models.IntegerField(choices=matched.choices, blank=True, null=True)

class PartnerPref(models.Model):
    Cust_id = models.OneToOneField(User, primary_key=True, unique=True, on_delete=models.CASCADE)
    Age_min = models.IntegerField()
    Age_max = models.IntegerField()
    #Height = models.DecimalField(max_digits=3, decimal_places=2)
    Religion = models.CharField(max_length=20)
    diets = models.IntegerChoices("diets", "Veg Non-Veg")
    Diet = models.IntegerField(choices=diets.choices)
    Income = models.IntegerField()

class Photos(models.Model):
    Cust_id = models.OneToOneField(User, primary_key=True, unique=True, on_delete=models.CASCADE)
    Pic1 = models.ImageField(upload_to="pics", null=True)
    Pic2 = models.ImageField(upload_to="pics", null=True)
    Pic3 = models.ImageField(upload_to="pics", null=True)
    Pic4 = models.ImageField(upload_to="pics", null=True)

class Feedback(models.Model):
    #id = models.IntegerField(primary_key=True)
    #Cust_id = models.OneToOneField(User, primary_key=True, unique=True, on_delete=models.CASCADE)
    Cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=200)
    Rating = models.IntegerField()


class Activities(models.Model):
    City = models.CharField(max_length=20, default='Bangalore', blank=True, null=False)
    Activity_Name = models.CharField(max_length=50)
    def __str__(self):
        return self.City
    
class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')