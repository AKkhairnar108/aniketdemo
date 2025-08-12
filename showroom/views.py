from django.shortcuts import render , redirect
from .models import Bike
from .forms import Bikeform
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    if request.method == 'POST':
        form = Bikeform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form=Bikeform()
    return render (request, 'add.html',{'form':form})
def bike_list(request):
    bikes = Bike.objects.all()
    return render(request,'bike_list.html',{'bikes' : bikes})
# def edit_bike(request, pk):
#     bike = get.object or 404(Bike, pk=pk)
#     form = BikeForm(request.POST or None, instance=bike)
#     if form.is_valid():
#         form.save()
#         return redirect('bike_list')
#     return render(request,'edit_bike.html',{'form':form})
# def delete_bike(request, pk):
#     bike = get.object.or 404(Bike, pk = pk)
#     if request.method == 'POST':
#         bike.delete()
#         return redirect('bike_list')
#     return render(request,'edit_bike.html',{'bike' : bike })

