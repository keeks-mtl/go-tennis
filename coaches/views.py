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

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added coach!')
            return redirect(reverse('add_coach'))
        else:
            messages.error(request, 'Failed to add coach. Please ensure the form is valid.')
    else:
        form = CoachForm()

    template = 'coaches/add_coach.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_coach(request, lesson_id):
    """ Edit a coach's information """
    coach = get_object_or_404(Coach, pk=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            coach = form.save()
            messages.success(request, 'Successfully updated coach!')
            return redirect(reverse('view_coaches'))
        else:
            messages.error(request, 'Failed to update coach. Please ensure the form is valid.')
    else:
        form = CoachForm(instance=coach)
        messages.info(request, f"You are editing a coach's informaiton")

    template = 'coaches/edit_coach.html'
    context = {
        'form': form,
        'coach': coach,
    }

    return render(request, template, context)


def delete_coach(request, coach_id):
    """ Delete a coach from the coaches page """
    coach = get_object_or_404(Coach, pk=coach_id)
    coach.delete()
    messages.success(request, 'Coach deleted!')
    return redirect(reverse('view_coaches'))
