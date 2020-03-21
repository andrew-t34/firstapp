from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    text = ''
    daddy = ''
    if 'questions' in request.session:
        del request.session['questions']
    return render(request, 'index.html', {'text': text,'daddy': daddy, 'id': 2 })
