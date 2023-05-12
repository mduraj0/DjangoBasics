from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login
from .forms import ContactForm, UserProfileForm


def hello(request):
    return render(request, 'main/hello.html')


def about(request):
    return render(request, 'main/about.html')


def some_test(request):
    age = 26
    first_name = 'Michael'
    children = ['Aniela', 'Rozalia', 'Julian']
    programming_l = {
        'python': 'advanced',
        'sql': 'beginner',
        'ml': 'beginner'
    }
    books = {'Clean code', 'biblia_mysql'}

    return render(request, 'main/some_test.html', context={
        'age': age,
        'first_name': first_name,
        'children': children,
        'programming_l': programming_l,
        'books': books
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            services.send_message(form.cleaned_data)
            return HttpResponseRedirect(reverse("contact"))
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {'form': form})


def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method == 'POST':
        try:
            profile = user.userprofile
            form = UserProfileForm(request.POST, instance=profile)
        except AttributeError:
            pass
        if form.is_valid():
            form.save()
    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=profile)
        except AttributeError:
            form = UserProfileForm(initial={"user": user, "bio": ""})
        if request.user != user:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []

    return render(request, "main/userprofile.html", {"form": form})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print('invalid loign')