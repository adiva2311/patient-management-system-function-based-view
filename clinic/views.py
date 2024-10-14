from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_title':'Home Page',
        'heading':'Klinik Sari Mutiara',
    }
    return render(request, 'index.html', context)