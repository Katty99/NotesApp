from django.shortcuts import render, redirect

from NotesApp.account.models import Account
from NotesApp.notes.models import Notes


# Create your views here.
def profile(request):
    account = Account.objects.first()
    total_notes = len(Notes.objects.all())
    context = {'account': account, 'total_notes': total_notes}
    return render(request, template_name='account/profile.html', context=context)


def delete_profile(request):
    account = Account.objects.first()
    notes = Notes.objects.all()
    account.delete()
    notes.delete()
    return redirect('home')
