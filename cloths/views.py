from django.shortcuts import render

app_name='dress'
# Create your views here.
def partywear(request):
    return render(request,'partywear.html')

def casualwear(request):
    return render(request,'casualwear.html')