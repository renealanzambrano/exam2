#-----------------------LIBRERIAS-----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#-----------------------MODELOS-------------------------
from Registro.models import Genero
from Registro.models import Ciudad
from Registro.models import Estado
from Registro.models import Civil

#--------------------SERIALIZERS--------------------------
from Registro.serializers import GeneroSerializers
from Registro.serializers import CiudadSerializers
from Registro.serializers import EstadoSerializers
from Registro.serializers import CivilSerializers
#-------------------------GENERO-----------------------------------
class GeneroList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Genero.objects.filter(delete=False)   
        serializer = GeneroSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class GeneroDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Genero.objects.get(pk=id)
        except Genero.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        gender = self.get_object(id)
        serializer = GeneroSerializers(gender)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        gender = self.get_object(id)
        serializer = GeneroSerializers(gender, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        gender = self.get_object(id)
        serializer = GeneroSerializers(gender, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # gender = self.get_object(id)
        # gender.delete()
        # return Response('Elemento Eliminado')
#-------------------------------------CIUDAD------------------------------------
class CiudadList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Ciudad.objects.filter(delete=False)   
        serializer = CiudadSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class CiudadDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Ciudad.objects.get(pk=id)
        except Ciudad.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        ciudad = self.get_object(id)
        serializer = CiudadSerializers(ciudad)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        ciudad = self.get_object(id)
        serializer = CiudadSerializers(ciudad, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        ciudad = self.get_object(id)
        serializer = CiudadSerializers(ciudad, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#----------------------------------------Estado-----------------------------------
class EstadoList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Estado.objects.filter(delete=False)   
        serializer = EstadoSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class EstadoDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Estado.objects.get(pk=id)
        except Estado.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        state = self.get_object(id)
        serializer = EstadoSerializers(state)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        state = self.get_object(id)
        serializer = EstadoSerializers(state, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        state = self.get_object(id)
        serializer = EstadoSerializers(state, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#-----------------------------CIVIL--------------------------------------------
class CivilList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Civil.objects.filter(delete=False)   
        serializer = CivilSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = CivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class CivilDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Civil.objects.get(pk=id)
        except Civil.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        civil = self.get_object(id)
        serializer = CivilSerializers(civil)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        civil = self.get_object(id)
        serializer = CivilSerializers(civil, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        civil = self.get_object(id)
        serializer = CivilSerializers(civil, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
