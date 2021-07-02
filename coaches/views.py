from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Coach, Comment
from .forms import CoachForm, CommentForm

# Create your views here.


def view_coaches(request):
    """ A view to return the coaches page """

    coaches = Coach.objects.all()

    context = {
        'coaches': coaches,
    }
    return render(request, 'coaches/coaches.html', context)


def view_coach(request, coach_id):
    """ A view to show a particular coaches page and their comments"""

    coach = get_object_or_404(Coach, pk=coach_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.coach = coach
            comment.author = request.user
            comment.stars = int(request.POST.get("stars"))
            form.save()
            messages.success(request, "Your comment has been added.")
            return redirect(reverse("view_coach", args=[coach_id]))
        else:
            messages.error(request,
                           "Error adding your comment please try again")
            return redirect(reverse("view_coach", args=[coach_id]))
    comments = Comment.objects.filter(coach=coach)

    form = CommentForm()

    context = {
        "coach": coach,
        "form": form,
        "comments": comments
    }

    return render(request, 'coaches/coach.html', context)


@login_required
def add_coach(request):
    """ Add a coach to the coaches page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            coach = form.save()
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


@login_required
def edit_coach(request, coach_id):
    """ Edit a coach's information """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_coach(request, coach_id):
    """ Delete a coach from the coaches page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    coach = get_object_or_404(Coach, pk=coach_id)
    coach.delete()
    messages.success(request, 'Coach deleted!')
    return redirect(reverse('view_coaches'))
