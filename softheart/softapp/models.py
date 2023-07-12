from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
# Create your models here.



class Course(models.Model):
   title              = models.CharField(max_length=200)
   description        = models.TextField(null=True, blank=True)
   course_thumbnail   = models.ImageField(validators = [FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)
   current_price      = models.IntegerField(default=0)
   category           = models.ManyToManyField('Category')
   id                 = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

   def __str__(self):
        return self.title
    
    
   class Meta:
      verbose_name = 'course'
      verbose_name_plural = 'bootcamp course'



class Category(models.Model):
   category_name = models.CharField(max_length=50, unique=True)
   id            = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   
   def __str__(self):
        return self.category_name