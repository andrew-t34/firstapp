from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    text = ''
    daddy = ''
    if 'questions' in request.session:
        del request.session['questions']
    if 'user_answers' in request.session:
        del request.session['user_answers']
    return render(request, 'index.html', {'text': text,'daddy': daddy, 'id': 2 })
