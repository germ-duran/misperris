from django.shortcuts import render, redirect
from.models import Region, Ciudad, Persona,Raza,Mascota,EstadoMascota,GeneroMascota
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):

    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()

    variables  = {
        'regiones':regiones,
        'ciudades':ciudades
    }



    #preguntaremos si es POST
    if request.POST:
        #si la peticion es POST obtendremos los datos
        personas = Persona()
        personas.nombre = request.POST.get('txtNombre')
        personas.run = request.POST.get('txtRun')
        personas.correo = request.POST.get('txtCorreo')
        personas.telefono  = request.POST.get('txtTelefono')
        #la region es una colaboracion de clases
        #por lo tanto para obtener el combo primero
        #crearemos un objeto region
        regiones = Region()
        regiones.id  = request.POST.get('cboRegion')
        #guardamos la marca completo dentro del auto
        personas.regiones = Region
        ciudades  = Ciudad()
        ciudades.id  = request.POST.get('cboCiudad')
        #guardamos la marca completo dentro del auto
        personas.Ciudad = ciudades
        
        #procedemos a guardar el auto en la BBDD
        try:
            personas.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"
   
    return render(request,'core/formulario.html',variables)        



def listar_personas(request):
    personas = Persona.objects.all()
        
    return render(request, 'core/listar_personas.html',{
        'personas':personas})  


def eliminar_personas(request,id):
    personas = Persona.objects.get(id=id)

    try:
        personas.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)

    except:
        mensaje = "No se ha podido eliminar"    
        messages.error(request, mensaje)
    return redirect ('listar_personas')
 



def modificar_personas(request, id):

    personas = Persona.objects.get(id=id)
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()

    variables = {
        'personas':personas,
        'regiones':regiones,
        'ciudades':ciudades
    }
    #preguntaremos si es POST
    if request.POST:
        #si la peticion es POST obtendremos los datos
        personas = Persona()
        personas.id = request.POST.get('txtId')
        personas.run = request.POST.get('txtRun')
        personas.correo = request.POST.get('txtCorreo')
        personas.telefono  = request.POST.get('txtTelefono')
        #la region es una colaboracion de clases
        #por lo tanto para obtener el combo primero
        #crearemos un objeto region
        regiones = Region()
        regiones.id  = request.POST.get('cboRegion')
        #guardamos la marca completo dentro del auto
        personas.regiones = Region
        ciudades  = Ciudad()
        ciudades.id  = request.POST.get('cboCiudad')
        #guardamos la marca completo dentro del auto
        personas.ciudades = Ciudad

        #procedemos a guardar el auto en la BBDD
        try:
            personas.save()
            messages.success(request,'modificado correctamente ')
        except:
           messages.error(request,'no se ha podido guardar')
        return redirect('listar_personas')   
    return render(request,'core/modificar_personas.html')


def agregarMascota(request):
    
    raza = Raza.objects.all()
    estado = EstadoMascota.objects.all()
    genero = GeneroMascota.objects.all()
    
    variables = {
        'raza': raza,
        'estado':estado,
        'genero':genero
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombre = request.POST.get('txtNomMascota')
        mascota.ingreso = request.POST.get('txtFechaIng')
        mascota.nacimiento = request.POST.get('txtFechaNac')
        mascota.imagen = request.FILES.get('txtImagen')
        
        #mascota.raza = raza
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.Raza = raza
        
        #mascota.estado = estado
        estado = EstadoMascota()
        estado.id = request.POST.get('cboEstado')
        mascota.EstadoMascota = estado

        #mascota.genero = genero
        genero = GeneroMascota()
        genero.id = request.POST.get('cboGenero')
        mascota.GeneroMascota = genero
        
        try:
            mascota.save()           
            variables['mensaje'] = "Guardado correctamente"
        except:
            
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/agregarMascota.html',variables)

def listarMascotas(request):

    mascota = Mascota.objects.all()
        
    return render(request, 'core/listarMascotas.html',{
        'mascota':mascota})  


def modificarMascotas(request,id):
    mascota = Mascota.objects.get(id=id)
    raza = Raza.objects.all()
    estado= EstadoMascota.objects.all()
    genero = GeneroMascota.objects.all()
    
    variables = {
        'mascota':mascota,
        'raza': raza,
        'estado':estado,
        'genero':genero
    }

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombre = request.POST.get('txtNomMascota')
        mascota.ingreso = request.POST.get('txtFechaIng')
        mascota.nacimiento = request.POST.get('txtFechaNac')
        
        #mascota.raza = raza
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        
        #mascota.estado = estado
        estado = EstadoMascota()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado

        #mascota.genero = genero
        genero = GeneroMascota()
        genero.id = request.POST.get('cboGenero')
        mascota.genero = genero
        
        try:
            mascota.save()           
            messages.success(request, 'modifico correctamente')
        except:
            
            messages.error(request, 'No se ha podido modificar')
        return redirect('listarMascotas')

    
    return render(request, 'core/modificarMascotas.html',variables)
  
def eliminarMascota(request,id):
    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se a podido eliminar"
        messages.error(request, mensaje)

    return redirect('listarMascotas')

