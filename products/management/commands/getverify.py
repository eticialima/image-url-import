from django.core.management.base import BaseCommand
from products import models
import json

class Command(BaseCommand): 
    help = 'Data import from json file and create instance for products image'

    def handle(self, *args, **options):
        with open('sample.json') as f:
            sample = json.load(f)
            for item in sample:
                prod = models.Product.objects.create( 
                title=item['title'],
                description=item['description'],
                category=models.Category.objects.get_or_create(name="Rolex")[0],
                )    
                image = item['image'][0]
                models.Image.objects.create(
                    product=prod,
                    image_url=image,
                )   
                print("CREATE INSTANCE!!!")