from django.shortcuts import render

from .forms import ArticuloForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

# Create your views here.


#def Reporte(request):
 #   return render(request,'template.html')


def crear(request):
    if request.POST:
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = ArticuloForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request,'template.html', args)

