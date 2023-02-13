import django.http
from django.shortcuts import render
from . import util
from .forms.encyclopedia import forms
from django.core import files


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    if name.lower() in (name.lower() for name in util.list_entries()):
        return render(request, "encyclopedia/entry.html", {
            "name": name,
            "body_text": util.md_to_html(util.get_entry(name))
        })
    else:
        return render(request, "encyclopedia/error.html")


def new_entry(request):
    if request.method == "POST":
        form_data = forms.NewEntryForm(request.POST)
        form_data.is_valid()
        entry_name = form_data.cleaned_data['entry_name']
        if entry_name.lower() in (name.lower() for name in util.list_entries()):
            return django.http.HttpResponse(f"Entry {entry_name} already exists")
        else:
            entry_content = form_data.cleaned_data['entry_content']
            with open(f'entries/{entry_name}.md', 'w') as f:
                newFile = files.File(f)
                newFile.write(entry_content)
            return entry(request, entry_name)

    else:
        return render(request, "encyclopedia/new_entry.html", {
            'form': forms.NewEntryForm()
    })


def random(request):
    return render(request, "encyclopedia/error.html")