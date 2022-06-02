from django.db import models

# Create your models here.


class Correo(models.Model):
    empresa=models.CharField(max_length=200)
    correo_cliente=models.CharField(max_length=200)
    correo_admin=models.CharField(max_length=200)
    mensaje=models.CharField(max_length=200)
    asunto=models.CharField(max_length=200)

    creado=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.empresa) + str(self.creado)
