from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, CarForm, UserRegisterForm
from .models import Car

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)

    form = ContactForm()
    return render(request,'form.html',{'form': form})

def car_detail(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()

    form = CarForm()
    return render(request,'form.html',{'form': form})

def car_list_view(request):
    queryset = Car.objects.all()
    context = {
        "object_list":queryset
    }
    return render (request, "car_list.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car')
    else:
        form = UserRegisterForm()

    return render(request,"register.html", {'form': form})

# Create your views here.
