from django.db.models import *
from django_pgjsonb import JSONField as JSONBField

class DummyData(models.Model):
    num_of_people = PositiveIntegerField() 
    budget = DecimalField(max_digits=10, decimal_places=2) 
    # meta = JSONBField([null=True, default={}]) 
