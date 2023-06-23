from django.shortcuts import render, redirect

from NotesApp.account.forms import AccountForm
from NotesApp.account.models import Account
from NotesApp.notes.models import Notes


# Create your views here.


def home_with_profile(request):
    account = Account.objects.first()
    notes = Notes.objects.all()
    context = {
        'account': account,
        'notes': notes
    }
    return render(request, template_name='common/home-with-profile.html', context=context)


def home_without_profile(request):
    account = Account.objects.first()
    if request.method == 'GET':
        form = AccountForm()

    else:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'account': account
    }
    return render(request, template_name='common/home-no-profile.html', context=context)


def home(request):
    account = Account.objects.first()
    if account:
        return home_with_profile(request)
    else:
        return home_without_profile(request)
