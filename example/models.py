# Create your models here.
from django.db import models

class Sample(models.Model):
    # This will use a normal <textarea> when rendered in a (Model)Form
    plain_body = models.TextField(blank=True, verbose_name='plain version')
    another_body = models.TextField(blank=True, verbose_name='another version')
