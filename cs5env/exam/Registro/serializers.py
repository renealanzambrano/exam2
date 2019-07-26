from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin
#-----------MODELOS---------------------------------
from Registro.models import Genero
from Registro.models import Ciudad
from Registro.models import Estado
from Registro.models import Civil

class GeneroSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__');
class CiudadSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__');
class EstadoSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__');
class CivilSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    nombreGenero= serializers.ReadOnlyField(source="genero_pk.genero1")
    nombreCiudad= serializers.ReadOnlyField(source="city_pk.city")
    nombreEstado= serializers.ReadOnlyField(source="relation_pk.relation")
    class Meta:
        model = Civil
        fields = ('__all__');
