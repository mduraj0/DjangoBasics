from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(self, *args, **kwargs)
            self.helper = FormHelper
            self.helper.form_method = 'post'
            self.helper.form_action = 'book:add'
            self.helper.add_input(Submit('submit', 'wyślij'))