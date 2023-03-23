from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserContentChoice:
    LEFT = 1
    RIGHT = 2
    choices = (
        (LEFT, "Left"),
        (RIGHT, "Right"),
    )
class HeroPage(models.Model):
    image_title = models.CharField(
        max_length=55,
        blank = True,
        null = True
        )
    user_content = models.PositiveIntegerField(
        choices=UserContentChoice.choices
    )
    image_sub_title = models.CharField(
        max_length=55,
        blank = True,
        null = True
        )
    short_description = models.TextField(
        _("Hero Image Description"), null=True, blank=True
    )
    image = models.ImageField(default='default.jpeg', upload_to='hero')
    is_displayed = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.image_title
    

class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length = 55)
    subject = models.CharField(max_length = 55)
    email = models.EmailField()

    def __str__(self):
        return self.email