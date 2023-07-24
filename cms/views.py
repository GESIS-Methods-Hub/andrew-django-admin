from django.http import HttpResponse

def add_content(request):
    return HttpResponse("You're looking at")
