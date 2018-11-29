from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
       return self.nombre
    
    class Meta:
     verbose_name="Region"
     verbose_name_plural = "Regiones"       

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    Region  = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    def __str__(self):
       return self.nombre

    class Meta:
     verbose_name="Ciudad"
     verbose_name_plural = "Ciudades"    

class Persona(models.Model):
    run = models.CharField(max_length=12, unique=True)
    nombre  = models.CharField(max_length=30)
    correo  = models.CharField(max_length=30)
    telefono  = models.IntegerField()
    #clave foranea
    Ciudad  = models.ForeignKey(Ciudad, on_delete=models.CASCADE)



    def __str__(self):
        return self.run


class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class EstadoMascota(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
       return self.nombre

class GeneroMascota(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
       return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    ingreso = models.CharField(max_length=50)
    nacimiento = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="mascota", null=True)
    
    
    Raza = models.ForeignKey(Raza, on_delete=models.CASCADE, null=True)
    GeneroMascota = models.ForeignKey(GeneroMascota, on_delete=models.CASCADE,null=True)
    EstadoMascota = models.ForeignKey(EstadoMascota, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre


