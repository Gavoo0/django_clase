from django.shortcuts import render,redirect
from .models import Alumno,Genero,Ramo
from .forms import RamoForm,SeccionForm
# Create your views here.
def index(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,'alumnos/index.html',context)

def listadoSQL(request):
    alumnos=Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    context={"alumnos":alumnos}
    return render(request,'alumnos/index.html',context)

def crud(request):
    alumnos=Alumno.objects.all()
    context={'alumnos':alumnos}
    return render(request,'alumnos/alumnos_list.html',context)

def alumnosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=apaterno,
            apellido_materno=amaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,  # Asociar el genero correctamente
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )
        obj.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'alumnos/alumnos_add.html', context)

def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)
        alumno.delete()
        mensaje='Datos Eliminados'
        alumnos=Alumno.objects.all()
        context={"mensaje":mensaje}
        return render(request,'alumnos/alumnos_list.html',context)
    except:
        mensaje='Eror, no existe el rut...'
        alumnos=Alumno.objects.all()
        context={"alumnos":alumnos,
                 "mensaje":mensaje}
        return render(request,'alumnos/alumnos_list.html',context)


def alumnos_findEdit(request,pk):
    if pk !="":
        alumno=Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()
        print(type(alumno.id_genero.genero))
        context={"alumnos":alumno,
                 "generos":generos}
        if alumno:
            return render(request,'alumnos/alumnos_findEdit.html',context)
        else:
            context={"mensaje":'Eror, no existe el rut...'}
            return  render(request,'alumnos/alumnos_findEdit.html',context)


def alumnosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre = nombre
        alumno.apellido_paterno = apaterno
        alumno.apellido_materno = amaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero  # Asociar el genero correctamente
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = activo
        alumno.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Datos actualizados",
            'generos': generos,
            'alumno': alumno
        }
        return render(request, 'alumnos/alumnos_findEdit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)


def crud_ramo(request):
    ramo=Ramo.objects.all()
    context={"ramo":ramo}
    return render(request,'alumnos/crud_ramo.html',context)


def formRamo(request):
    context={}
    if request.method=="POST":
        form=RamoForm(request.POST)
        if form.is_valid:
            print("ola")
            form.save()
            form=RamoForm()
            context={"mensaje":'Ok, datos grabados...',
                     "form":form}
            return render(request,"alumnos/formRamo.html",context)
    else:
        form=RamoForm()
        context={"form":form} 
        return render(request,"alumnos/formRamo.html",context)


def ramo_del(request,pk):
    context={}
    try:
        ramo=Ramo.objects.get(id_ramo=pk)
        ramo.delete()
        mensaje='Ramo eliminado'
        ramo=Ramo.objects.all()
        context={"mensaje":mensaje,
                 "ramo":ramo}
        return render(request,'alumnos/crud_ramo.html',context)
    except:
        mensaje='No existe el ramo'
        ramo=Ramo.objects.all()
        context={"mensaje":mensaje,
                 "ramo":ramo}
        return render(request,'alumnos/crud_ramo.html',context)
    

def seccion_form(request):
    context={}
    if request.method=="POST":
        form=SeccionForm(request.POST)
        if form.is_valid:
            print("ola")
            form.save()
            form=SeccionForm()
            context={"mensaje":'Ok, datos grabados...',
                     "form":form}
            return render(request,"alumnos/seccion_form.html",context)
    else:
        form=SeccionForm()
        context={"form":form} 
        return render(request,"alumnos/seccion_form.html",context)

