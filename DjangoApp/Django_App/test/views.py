from django.shortcuts import render
from .models import Test1
from .forms import TestForm

def index(request):
    data = Test1.objects.all()
    params = {
        'title':'Hello',
        'message':'all Tests.',
        'form':TestForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Test1.objects.get(id=num)
        params['data'] = [item]
        params['form'] = TestForm(request.POST)
    else:
        params['data'] = Test1.objects.all()
    return render(request, 'test/index.html', params)