
	from django.db import models

# Create your models here.
class Estudiante(models,Models):
	nombre= models.Charfield(max_length=200)
	apellidos= models.Charfield(max_length=200)
	edad= models.Charfield(default=0)
	grado= models.Charfield('grados.Grado')

	def __str__(self):
		return "%S %S - %S" %(
			self.nombre
			self.grado
			self.apellidos
			self.edad)
		

