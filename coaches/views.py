from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Coach

# Create your views here.


def view_coaches(request):
    """ A view to return the coaches page """

    coaches = Coach.objects.all()

    context = {
        'coaches': coaches,
    }
    return render(request, 'coaches/coaches.html', context)
