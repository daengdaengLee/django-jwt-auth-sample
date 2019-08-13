from django.http import HttpResponse


def echo_username(request):
    return HttpResponse("Who are you?")
