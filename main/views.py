from django.shortcuts import render, redirect
from .forms import AllForm

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = AllForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    
    form = AllForm()
    
    data = {
        'form' : form
    }
    
    return render(request, 'main/index.html', data)