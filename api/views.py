from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.
from django.core import serializers
import json
from core.models import *


from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from fcm_django.models import FCMDevice



@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    body = request.body.decode('utf-8')

    bodyDict = json.loads(body)

    mascota = Mascota()
    mascota.nombre = bodyDict['nombre']
    mascota.ingreso = bodyDict['ingreso']
    mascota.nacimiento = bodyDict['nacimiento']
    mascota.Raza = Raza(id=bodyDict['Raza_id'])
    mascota.EstadoMascota = EstadoMascota(id=bodyDict['EstadoMascota_id'])
    mascota.GeneroMascota = GeneroMascota(id=bodyDict['GeneroMascota_id'])

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")



def listar_mascotas(request):
    mascota = Mascota.objects.all()

    mascotaJson = serializers.serialize('json', mascota)

    return HttpResponse(mascotaJson, content_type="application/json")



@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminado correctamente'}),
        content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"no se ha podido eliminar"}),
        content_type="application/json")


@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    body = request.body.decode('utf-8')
    
    bodyDict = json.loads(body)

    mascota = Mascota()
    mascota.id = bodyDict['id']
    mascota.nombre = bodyDict['nombre']
    mascota.ingreso = bodyDict['ingreso']
    mascota.nacimiento = bodyDict['nacimiento']
    mascota.Raza = Raza(id=bodyDict['Raza_id'])
    mascota.EstadoMascota = EstadoMascota(id=bodyDict['EstadoMascota_id'])
    mascota.GeneroMascota = GeneroMascota(id=bodyDict['GeneroMascota_id'])

    try:
        auto.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido modificar'}), content_type="application/json")


