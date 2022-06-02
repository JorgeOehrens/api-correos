from rest_framework import serializers
from base.models import Correo


class CorreoSerializacion(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields ='__all__'