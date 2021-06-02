from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Lesson, ClassType

# Create your views here.


def lessons(request):
    """ A view to return the index page """

    return render(request, 'lessons/lessons.html')
