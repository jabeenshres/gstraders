from django.db import models
from PIL import Image
from datetime import datetime


# Create your models here.

class Products(models.Model):
    date = models.DateTimeField(default = datetime.now)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default='default.jpeg', upload_to='trending')

    def __str__(self):
        return self.product_name

    #Resizing the image 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 335:
            output_size = (300, int(336.53))
            img = img.resize(output_size, Image.ANTIALIAS)
            img.save(self.image.path)

    #Resizing the image if there is default image

        if self.image.name == 'default.jpeg':
            img = Image.open(self.image.path)
            output_size = (300, int(336.53))
            img = img.resize(output_size, Image.ANTIALIAS)
            img.save(self.image.path)
