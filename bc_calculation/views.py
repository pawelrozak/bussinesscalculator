from django.http import HttpResponse


def index(request):
    return HttpResponse("Here will be possibilities of computation.")