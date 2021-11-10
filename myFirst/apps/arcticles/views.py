from django.http import HttpResponse

def index(request):
    return HttpResponse("Сәлем, Әлем!")

def test(request):
    return HttpResponse("Сынама парақша!")