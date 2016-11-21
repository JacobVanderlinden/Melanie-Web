from django.db import models

def get_image_path(instance, filename):
	return 'melanie/images/%s' % (filename)

# Create your models here.
class Mole(models.Model):
	image = models.ImageField(upload_to=get_image_path)