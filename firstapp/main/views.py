from django.shortcuts import render

# Create your views here.
def index(request):
    text = 'А это переданная переменная'
    return render(request, 'index.html', {'text': text})
