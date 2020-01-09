from django.db import models

# Create your models here.

class Family_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Traffic_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Government_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Army_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Labor_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Financial_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Trade_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Leisure_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Lawsuit_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Welfare_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Estate_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Business_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Crime_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Client_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Children_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Information_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Startup_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
class Eco_Board(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()