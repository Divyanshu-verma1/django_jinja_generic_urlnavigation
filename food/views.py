from django.shortcuts import render

app_name = 'veg_food'
# Create your views here.
def veg(request):
    return render(request,'veg.html')

def nonveg(request):
    return render(request,'nonveg.html')