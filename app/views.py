from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'This is fiLters Concept','c':1,'dt':dt}
    return render(request,'built_in-filters.html',d)
