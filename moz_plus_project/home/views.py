from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


from . import forms


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def user_login(request):
    if request.method != 'POST':
        form = forms.LoginForm()
    else:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            auth = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )

            if auth is not None:
                login(request, auth)
                if request.user.groups.all().first().name == 'content_creator':
                    return redirect('content_creator:content_creator')
                elif request.user.groups.all().first().name == 'subscriber':
                    return redirect('subscriber:subscriber')

    context = {'form': form}
    return render(request, 'registration/login.html', context)


def subscriber_registration(request):
    if request.method != 'POST':
        form = forms.UserRegistrationForm()
    else:
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            group_reviewer = Group.objects.get(name='subscriber')
            new_user.groups.add(group_reviewer)

            return redirect('subscriber:subscriber')

    context = {'form': form}
    return render(request, 'accounts/user_registration.html', context)


def creator_registration(request):
    if request.method != 'POST':
        form = forms.CreatorRegistrationForm()
    else:
        form = forms.CreatorRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            group_reviewer = Group.objects.get(name='content_creator')
            new_user.groups.add(group_reviewer)

            return redirect('content_creator:content_creator')

    context = {'form': form}
    return render(request, 'accounts/creator_registration.html', context)

