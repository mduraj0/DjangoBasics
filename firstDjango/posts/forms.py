from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.helper import FormHelper
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=AutocompleteSelectMultiple(
            Post._meta.get_fiel('tags'),
            admin.AdminSite(),
        )
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
                'Dodaj post',
                'title',
                'content',
                'published',
                'sponsored',
                'image',
                'tags',
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
