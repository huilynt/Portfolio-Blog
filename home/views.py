from django.shortcuts import render

def home_index(request):
    return render(request, 'home.html', {})
