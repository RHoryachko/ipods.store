from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.IntegerField()
    image1 = models.ImageField('Картинка1', upload_to='posts/',blank=True) 
    image2 = models.ImageField('Картинка2', upload_to='posts/',blank=True)  
    image3 = models.ImageField('Картинка3', upload_to='posts/',blank=True) 
    image4 = models.ImageField('Картинка4', upload_to='posts/',blank=True) 
    image5 = models.ImageField('Картинка5', upload_to='posts/',blank=True) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title