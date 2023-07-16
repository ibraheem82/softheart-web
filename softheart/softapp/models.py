import os
from PIL import Image
from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
# Create your models here.


def upload_path(instance, filename):
    # Define the upload path for the course thumbnail
    # You can customize this according to your requirements
    return f'course_thumbnails/{instance.id}/{filename}'
 
 
 
 
class Course(models.Model):
   title              = models.CharField(max_length=200)
   description        = models.TextField(null=True, blank=True)
   course_thumbnail   = models.ImageField(upload_to=upload_path, validators = [FileExtensionValidator(['png', 'jpg'])], null=True, blank=True)
   current_price      = models.IntegerField(default=0)
   category           = models.ManyToManyField('Category')
   id                 = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   def save(self, *args, **kwargs):
         super().save(*args, **kwargs)
         if self.course_thumbnail:
            # Resize the uploaded image after saving the model instance
            self.resize_image()

   def resize_image(self):
        # Open the uploaded image using PIL
        image = Image.open(self.course_thumbnail.path)

        # Define the desired dimensions for the resized image
        # You can customize these dimensions according to your requirements
        max_width = 800
        max_height = 600

        # Resize the image while preserving the aspect ratio
        image.thumbnail((max_width, max_height), Image.ANTIALIAS)

        # Save the resized image, overwriting the original file
        image.save(self.course_thumbnail.path)

        # You can also save the resized image to a different location if needed
        # new_image_path = f'some/other/path/{self.course_thumbnail.name}'
        # image.save(new_image_path)

        # Update the image field to reflect the resized image
        self.course_thumbnail.name = os.path.basename(self.course_thumbnail.path)
        self.save()


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