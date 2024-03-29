from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            permission = Permission.objects.get(name='Can add tag')
            user.user_permissions.add(permission)
        return redirect(reverse('main:hello'))

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
