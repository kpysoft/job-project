from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def bangalorejob(request):
    s='<h3>Currenlty there are 2 opening are available:<br>1)Java developer  2)Python Developer</h3>'

    return HttpResponse(s)

def punejob(request):
    s='<h3>Currenlty there are 2 opening are available:<br>1)Javascript developer  2)angular Developer</h3>'

    return HttpResponse(s)

def suratjob(request):
        s='<h3>Currenlty there are 2 opening are available:<br>1)BDE  2)Junior BDE</h3>'

        return HttpResponse(s)
