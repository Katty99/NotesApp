from django import forms

from NotesApp.notes.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'


class DeleteNotesForm(NotesForm):
    class Meta:
        model = Notes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
