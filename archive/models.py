from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.

class RecordManager(Owner):
    is_admin     = models.BooleanField()

class Group(Ownable):
    creator       = models.ForeignKey(RecordManager)
    creation_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)])
    name          = models.CharField(max_length=20)
    faculty       = models.CharField(max_length=100)
    def group

class Student(Ownable):
    creator = models.ForeignKey(RecordManager)
    name    = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group   = models.ForeignKey(Group)