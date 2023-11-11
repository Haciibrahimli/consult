from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255,verbose_name='xidmet adi')
    description = models.TextField(verbose_name='movzu')
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.title
class Meta:

    ordering = ('title',)
    verbose_name = 'xidet adi'
    verbose_name_plural = 'xidmet adlari'

class Quota(models.Model):
    name = models.CharField(max_length=255,verbose_name='ad')
    email = models.EmailField(verbose_name='email adresi')
    service = models.CharField(max_length=255,verbose_name='xidmetler')

    def __str__(self):
        return self.name
    
class Meta:

    ordering = ('name',)
    verbose_name = 'quota'
    verbose_name_plural = 'quotalar'

class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name='basliq')
    description = models.TextField(verbose_name='movzu')
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.title
    
class Meta:

    ordering = ('title',)
    verbose_name = 'bloq'
    verbose_name_plural = 'bloqlar'


class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    

    def __str__(self):
        return self.name
    
class Meta:

    ordering = ('name',)
    verbose_name = 'contact'
    verbose_name_plural = 'contactlar'






    
