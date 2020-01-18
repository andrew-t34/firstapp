from django.shortcuts import render

# Create your views here.
def index(request):
    text = ''
    daddy = ''
    return render(request, 'index.html', {'text': text,'daddy': daddy, 'id': 2 })
