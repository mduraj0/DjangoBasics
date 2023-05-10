from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.helper import FormHelper
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django import forms
from dal import autocomplete
from .models import Post
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url="tags:tag-autocomplete")
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            Fieldset(
                'Add post',
                'title',
                'content',
                'published',
                'sponsored',
                'image',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'Add', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
