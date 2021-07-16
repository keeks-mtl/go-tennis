from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Lesson, ClassType, Coach
from .forms import LessonForm

# Create your views here.


def lessons(request):
    """ A view to return the index page """

    return render(request, 'lessons/lessons.html')


def book_lessons(request):
    """ A view to return the book lessons page """

    lessons = Lesson.objects.all().order_by("date")
    coaches = Coach.objects.all()
    class_types = ClassType.objects.all()
    class_type_search = None
    sort = None
    sort_label = None
    direction = None
    coach_name = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'coach':
                sortkey = 'lower_coach'
                lessons = lessons.annotate(lower_coach=Lower('coach'))
            if sortkey == 'class_type':
                sortkey = 'class_type__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            lessons = lessons.order_by(sortkey)

        if 'class_type' in request.GET:
            class_type_search = request.GET['class_type']
            lessons = lessons.filter(class_type__name=class_type_search)
            sort_label = class_type_search
            class_type_search = ClassType.objects.filter(
                name__in=class_type_search)

        if 'coach' in request.GET:
            coach_name = request.GET['coach']
            coach_name = int(coach_name)
            lessons = lessons.filter(coach=coach_name)

    current_sorting = f'{sort}_{direction}'

    context = {
        'lessons': lessons,
        'coaches': coaches,
        'current_class_types': class_type_search,
        'current_coach_name': coach_name,
        'current_sorting': current_sorting,
        'class_types': class_types,
        'sort_label': sort_label,
    }

    return render(request, 'lessons/book.html', context)


@login_required
def add_lesson(request):
    """ Add a lesson to the booking page """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added lesson!')
            return redirect(reverse('add_lesson'))
        else:
            messages.error(request, (
                'Failed to add lesson. Please ensure the form is valid.'))
    else:
        form = LessonForm()

    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_lesson(request, lesson_id):
    """ Edit a lesson in the store """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff members can do that.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Successfully updated Lesson!')
            return redirect(reverse('book_lessons'))
        else:
            messages.error(request, (
                'Failed to update lesson. Please ensure the form is valid.'))
    else:
        form = LessonForm(instance=lesson)
        messages.info(request, f'You are editing a lesson on {lesson.date}')

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)


@login_required
def delete_lesson(request, lesson_id):
    """ Delete a lesson from the store """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, only staff members can do that.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    lesson.delete()
    messages.success(request, 'Lesson deleted!')
    return redirect(reverse('book_lessons'))
