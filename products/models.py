from django.db import models    
from django.core.files import File 
from urllib.request import urlopen
from urllib.parse import urlparse 
from tempfile import NamedTemporaryFile  

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField('Título',max_length=100)
    description = models.TextField('Descrição')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, 
        related_name='product')   

    def __str__(self):
        return self.title  

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True) 
    image = models.ImageField(upload_to='image', null= True, blank=True)
    image_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.product.title   

    def download_image(self, url):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(self.image_url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        name = urlparse(self.image_url).path.split('/')[-1]
        self.image.save(name, File(img_tmp), save=False)
 
    def save(self, *args, **kwargs):
        self.download_image(self.image_url)
        super(Image, self).save(*args, **kwargs) 