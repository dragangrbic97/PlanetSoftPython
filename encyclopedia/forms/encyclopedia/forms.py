from django import forms


class NewEntryForm(forms.Form):
    entry_name = forms.CharField(label="entry_name")
    entry_content = forms.CharField(label="entry_content", widget=forms.Textarea())
