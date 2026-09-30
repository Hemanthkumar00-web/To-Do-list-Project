from django.db import models

# Create your models here.

"""
task_name=string
is_completed=true/false
due_date=date column
created_date=date column(auto populate)

"""
class task(models.Model):
    task_name= models.CharField(max_length=100)
    is_completed= models.BooleanField(default=False)
    due_date= models.DateField()
    created_date= models.DateField(auto_now=True)


class cars(models.Model):
    cars_names=models.CharField(max_length=50)
    

