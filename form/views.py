from django.shortcuts import render
from .models import Form
from .forms import formdata
# Create your views here.
def home1(request):
    if request.method == 'POST':
        # name = request.post.get('name')
        # email = request.post.get('email')
        # date = request.post.get('date')
        # city = request.post.get('city')
        # phone = request.post.get('phone')
        form = formdata(request.POST or None)
        if form.is_valid():
            form.save()   
        
    obj = Form.objects.all()
    return render(request,'home1.html',{'obj':obj})