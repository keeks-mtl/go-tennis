from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Lesson, ClassType
from .forms import LessonForm

# Create your views here.


def lessons(request):
    """ A view to return the index page """

    return render(request, 'lessons/lessons.html')


def all_lessons(request):
    """ A view to return the book lessons page """

    lessons = Lesson.objects.all()
    class_types = None
    sort = None
    direction = None

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
            lessons = lessons.filter(class_type__name__in=class_types)

    current_sorting = f'{sort}_{direction}'

    context = {
        'lessons': lessons,
        'current_class_types': class_types,
        'current_sorting': current_sorting,
    }

    return render(request, 'lessons/book.html', context)


def add_lesson(request):
    """ Add a lesson to the booking page """
    
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added lesson!')
            return redirect(reverse('add_lesson'))
        else:
            messages.error(request, 'Failed to add lesson. Please ensure the form is valid.')
    else:
        form = LessonForm()

    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_lesson(request, lesson_id):
    """ Edit a lesson in the store """
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Lesson!')
            return redirect(reverse('lesson'))
        else:
            messages.error(request, 'Failed to update lesson. Please ensure the form is valid.')
    else:
        form = LessonForm(instance=lesson)
        messages.info(request, f'You are editing a lesson on {lesson.date}')

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)
