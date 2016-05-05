from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, y'all. You're at the moviedata index.")
