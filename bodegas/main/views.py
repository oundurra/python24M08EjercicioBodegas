from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from .forms import CustomUserCreationForm, TipoBodegaForm
from .models import TipoBodega
from .services import getNoticiasLikesByUser, addLike, removeLike

# Create your views here.
def index(request):
    noticias = getNoticiasLikesByUser(request.user.id)
    return render(request, 'index.html', {"user":request.user, "noticias":noticias})

@login_required
def cotizar(request):
    tipo_bodega_form = TipoBodegaForm()
    bodegas = []
    bodegas.append({"tipo":"Una"})
    bodegas.append({"tipo":"Dos"})
    return render(request, 'cotizar.html', {"user":request.user, "tipo_bodega_form":tipo_bodega_form, "bodegas":bodegas })

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