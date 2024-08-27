from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from .forms import CustomUserCreationForm, TipoBodegaForm, BodegaForm
from .models import TipoBodega, Bodega
from .services import getNoticiasLikesByUser, addLike, removeLike

# Create your views here.
def index(request):
    noticias = getNoticiasLikesByUser(request.user.id)
    return render(request, 'index.html', {"user":request.user, "noticias":noticias})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a homepage or another page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def add_like(request, user_id, noticia_id):
    addLike(user_id, noticia_id)
    return redirect('home')

def remove_like(request, user_id, noticia_id):
    removeLike(user_id, noticia_id)
    return redirect('home')

def cotizar(request):
    if request.method == 'POST':
        tipo_bodega = request.POST.get("tipo_bodega")

        tipo_bodega_form = TipoBodegaForm(request.POST)
        bodega_form = BodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        lista_bodega = request.POST.get("lista_bodega")

        if len(lista_bodega) > 0:
            lista_bodega = lista_bodega.split(',')
            bodegas_seleccionadas = Bodega.objects.filter(id__in=lista_bodega)
        else:
            bodegas_seleccionadas = ""

        lista_bodega = ','.join(lista_bodega)

        if request.POST.get("tipo_bodega") is not None:
            bodega_form.fields['bodega'].queryset = Bodega.objects.filter(tipo_bodega=tipo_bodega)
        else:
            bodega_form.fields['bodega'].queryset = None
        
        return render(request, 'cotizar.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "bodega_form":bodega_form, "lista_bodega":lista_bodega, "bodegas_seleccionadas":bodegas_seleccionadas})
    else:
        tipo_bodega_form = TipoBodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        lista_bodega = ""
        return render(request, 'cotizar.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "lista_bodega":lista_bodega})

def agregar_bodega(request):
    tipo_bodega_form = TipoBodegaForm(request.POST)
    bodega_form = BodegaForm()
    tipos_bodega = TipoBodega.objects.all()
    tipo_bodega = request.POST.get("tipo_bodega")

    if request.POST.get("bodega") is not None:
        bodega_form.fields['bodega'].queryset = Bodega.objects.filter(tipo_bodega=tipo_bodega)
        lista_bodega = request.POST.get("lista_bodega")

        if len(lista_bodega) > 0:
            lista_bodega = request.POST.get("lista_bodega").split(',')
        else:
            lista_bodega = []

        lista_bodega.append(request.POST.get("bodega"))
        bodegas_seleccionadas = Bodega.objects.filter(id__in=lista_bodega)
        lista_bodega = ','.join(lista_bodega)

    return render(request, 'cotizar.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "bodega_form":bodega_form, "lista_bodega":lista_bodega, "bodegas_seleccionadas":bodegas_seleccionadas})
    