from django import forms
from .models import Lesson, ClassType, Coach


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('class_type', 'coach',
                  'description', 'price',
                  'date', 'time', 'spots')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_type = ClassType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in class_type]
        coach = Coach.objects.all()
        first_names = [(c.id, c.get_first_name()) for c in coach]

        self.fields['class_type'].choices = friendly_names
        self.fields['coach'].choices = first_names
        self.fields['date'] = forms.DateField(widget=DateInput)
        self.fields['time'] = forms.TimeField(widget=TimeInput)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
