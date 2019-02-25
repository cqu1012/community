from django.shortcuts import render

# Create your views here.
def home(request):
    '''
    home page
    '''
    return render(request,'home/home.html')
