from django.http import HttpResponse


def index(request):
    for i in range (1,10):
        print ("f, {i} ahoj")
    return HttpResponse("Hello, world. You're at the polls index.")