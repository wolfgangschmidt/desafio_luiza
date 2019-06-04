from django.db import models

# Create your models here.
class Funcionario(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	dept = models.CharField(max_length=120)

	def __str__(self):
		return str(self.name)