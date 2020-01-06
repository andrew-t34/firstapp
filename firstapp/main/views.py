from django.shortcuts import render

# Create your views here.
def index(request):
    text = 'Здравствуй Владислав. Ты ЖОПА'
    daddy = 'А. Папа говно'
    return render(request, 'index.html', {'text': text,'daddy': daddy })
