from django.db import models

# Create your models here. 
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "approject"  

class PredResults(models.Model):
    Pregnancies = models.FloatField()	
    Glucose	= models.FloatField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
