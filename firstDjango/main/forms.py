from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.helper import FormHelper
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    send_to_me = forms.BooleanField(required=False)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'contact'
#         self.helper.layout = Layout(
#             Fieldset(
#                 'Dane kontaktowe',
#                 'email',
#             ),
#             Fieldset(
#                 'Zawartość',
#                 'title',
#                 'content'
#             ),
#             Fieldset(
#                 'Dodatkowe',
#                 HTML("Zaznacz jeśli chcesz by wysłać kopię wiadomości do Ciebie"),
#                 'send_to_me',
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Wyślij', css_class='btn btn-primary'),
#                 css_class="d-flex justify-content-end"
#             )
#         )
#         self.helper.add_input(Submit('submit', 'Wyślij'))


class PostForm(forms.Form):
    title = forms.CharField(label="Tytuł")
    content = forms.CharField(widget=forms.Textarea, label="Treść")
    published = forms.BooleanField(label="Opublikowany")
    sponsored = forms.BooleanField(label="Sponsorowany")

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
                'sponsored'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )
