from django.shortcuts import render

# Create your views here.

def people_directory(request):
    return render(request, 'people_directory.html')
