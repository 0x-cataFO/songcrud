from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You've successfully gotten to my site")