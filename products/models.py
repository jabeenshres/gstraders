from django.db import models
from PIL import Image
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# TODO we will use this model later in our project
# class Timestampable(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         abstract = True

#     def delete(self):
#         self.deleted_at = timezone.now()
#         super().save()


class Category(models.Model):
    title = models.CharField(_("Category Title"), max_length=255)
    slug = models.SlugField(_("Category Slug"), unique=True)
    description = models.TextField(
        _("Category Description"), null=True, blank=True
    )
    image = models.ImageField(default='default.jpeg', upload_to='category')
    is_displayed_in_trending = models.BooleanField(
        default=False
    )
    is_displayed_header = models.BooleanField(
        default=False
    )
    # TODO We will use this hierarchy later
    # parent = models.ForeignKey(
    #     "self", on_delete=models.CASCADE, null=True, blank=True,
    #     related_name='categories')

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Products(models.Model):
    date = models.DateTimeField(default = datetime.now)
    product_name = models.CharField(
        _("Product Name"),
        max_length=50
    )
    slug = models.SlugField(_("Category Slug"))
    description = models.TextField(
        _("Product Description"), null=True, blank=True
    )
    price = models.DecimalField(
        _("Product Price"),
        max_digits=8,
        decimal_places=2
    )
    discounted_price = models.DecimalField(
        _("Discounted price"),
        max_digits=8,
        decimal_places=2
    )
    image = models.ImageField(default='default.jpeg', upload_to='products')
    is_trending = models.BooleanField("Trending", default=False)
    is_liked = models.BooleanField("You may Like", default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super(Products, self).save(*args, **kwargs)

    # #Resizing the image 
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.width > 300 or img.height > 335:
    #         output_size = (300, int(336.53))
    #         img = img.resize(output_size, Image.ANTIALIAS)
    #         img.save(self.image.path)

    # #Resizing the image if there is default image

    #     if self.image.name == 'default.jpeg':
    #         img = Image.open(self.image.path)
    #         output_size = (300, int(336.53))
    #         img = img.resize(output_size, Image.ANTIALIAS)
    #         img.save(self.image.path)
