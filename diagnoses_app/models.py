from django.db import models

# Create your models here.

class DiagosticFeatures(models.Model):
    Age = models.IntegerField()
    Sex = models.IntegerField()
    chest_pain_type = models.IntegerField()
    BP = models.IntegerField()
    Cholesterol = models.IntegerField()
    FBS_over_120 = models.IntegerField()
    EKG_results = models.IntegerField()
    Max_HR = models.IntegerField()
    Exercise_angina = models.IntegerField()
    ST_depression = models.IntegerField()
    Slope_of_ST = models.IntegerField()
    Number_of_vessels_fluro = models.IntegerField()
    Thallium = models.IntegerField()


    