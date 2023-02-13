from django.shortcuts import render

from . import util


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
