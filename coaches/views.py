from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Coach
from .forms import CoachForm

# Create your views here.


def view_coaches(request):
    """ A view to return the coaches page """

    coaches = Coach.objects.all()

    context = {
        'coaches': coaches,
    }
    return render(request, 'coaches/coaches.html', context)


def add_coach(request):
    """ Add a coach to the coaches page """
    form = CoachForm()
    template = 'coaches/add_coach.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
