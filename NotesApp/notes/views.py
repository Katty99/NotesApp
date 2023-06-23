from django.shortcuts import render, redirect

from NotesApp.notes.forms import NotesForm, DeleteNotesForm
from NotesApp.notes.models import Notes


# Create your views here.
def add_notes(request):
    form = NotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, template_name='notes/note-create.html', context=context)


def edit_notes(request, id):
    note = Notes.objects.get(id=id)
    if request.method == 'GET':
        form = NotesForm(initial=note.__dict__)
        context = {'form': form}
        return render(request, template_name='notes/note-edit.html', context=context)
    else:
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, template_name='notes/note-edit.html', context=context)


def delete_notes(request, id):
    note = Notes.objects.get(id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    form = DeleteNotesForm(instance=note)
    context = {'form': form}
    return render(request, template_name='notes/note-delete.html', context=context)


def details_notes(request, id):
    note = Notes.objects.get(id=id)
    context = {'note': note}
    return render(request, template_name='notes/note-details.html', context=context)