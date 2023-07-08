from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
# Create your models here.



class Course(models.Model):
   title              = models.CharField(max_length=200)
   description        = models.TextField(null=True, blank=True)
   course_thumbnail   = models.ImageField(validators = [FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)
   initial_price      = models.IntegerField(default=0)
   current_price      = models.IntegerField(default=0)
   id                 = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)