from django import forms
from .widgets import CustomClearableFileInput
from .models import Coach, Comment


class CoachForm(forms.ModelForm):

    class Meta:
        model = Coach
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comment",
            "stars",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["comment"].widget.attrs[
            "placeholder"] = "Add a Comment here"
