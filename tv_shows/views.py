from django.shortcuts import render
from .models import Shows


def top_shows(request):
    show = Shows.objects.all()

    context = {
        'shows': show
    }
    return render(request, template_name="core/shows.html", context=context)
# Create your views here.
