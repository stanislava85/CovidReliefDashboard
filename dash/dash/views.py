from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def map(request):
    return render(request, 'map.html')

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
   return render(request, '500.html')

def handler403(request, exception):
    return render(request, '403.html')

def handler400(request, exception):
    return render(request, '400.html')