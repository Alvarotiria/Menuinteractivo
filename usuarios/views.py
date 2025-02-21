
#Esto es del sign up

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirige al login después del registro
    else:
        form = UserCreationForm()
    
    return render(request, "signup.html", {"form": form})