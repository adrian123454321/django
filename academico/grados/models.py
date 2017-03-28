from django.db import models
class Grados(models,Model):
	grado=models.Charfield(max_length=100)
	def __str__(self)
		return self.grado



