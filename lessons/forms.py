from django import forms
from .models import Lesson, ClassType


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_type = ClassType.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in class_type]

        self.fields['class_type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
