# functional based and classed based
from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("welcome to minksole , this is about us page")

def Blogs(request):
    return HttpResponse("Different blogs are created")