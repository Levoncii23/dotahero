from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. That's, my site")