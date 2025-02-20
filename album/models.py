from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

class Category(models.Model):
    """Categorias para clasificar las fotos"""
    name  = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Photo(models.Model):
    """ Fotos del album """
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.PROTECT   )
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.title
    """def get_absolute_url(self):
        return reverse('photo-list')"""
    @receiver(post_delete, sender=photo)
    def photo_delete(sender, instance, **kwargs):
        """Borra los ficheros de las fotos que se eliminen."""
        instance.photo.on_delete(False)
