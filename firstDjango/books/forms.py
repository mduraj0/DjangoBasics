from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete
from django import forms
from .models import Book
from tags.models import Tag


class BookForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )

    class Meta:
        model = Book
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(self, *args, **kwargs)
            self.helper = FormHelper
            self.helper.form_method = 'post'
            self.helper.form_action = 'book:add'
            self.helper.add_input(Submit('submit', 'wyślij'))