from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.helper import FormHelper
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image']
        labels = {
            'title': 'Tytuł',
            'content': 'Treść',
            'published': 'Opublikowany',
            'sponsored': 'Sponsorowany'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = 'posts:add'
        self.helper.layout = Layout(
            Fieldset(
                'Dane kontaktowe',
                'email',
            ),
            Fieldset(
                'Zawartość',
                'title',
                'content'
            ),
            Fieldset(
                'Dodatkowe',
                HTML("Zaznacz jeśli chcesz by wysłać kopię wiadomości do Ciebie"),
                'send_to_me',
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
