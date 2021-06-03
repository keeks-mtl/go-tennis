from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Lesson, ClassType

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
