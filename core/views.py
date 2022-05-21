from django.contrib.auth import login
from django.shortcuts import redirect, render

from . form import SignUpForm

# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    # se for igual a post isso que dizer q o form foi clicado
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        #verificar se e valido
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html',{'form': form})