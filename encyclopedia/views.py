from django.shortcuts import render, redirect
import markdown2
from . import util
import random

def index(request):
    return render(request, "index.html", {
        "entries": util.list_entries()
    })

def get_entry(request, title):
    content=util.get_entry(title)
    if content:

        return render(request, 'showentry.html', {'title': title, 'content': markdown2.markdown(content)})
    else:
        return render(request, 'error.html')

def edit(request, title):
    if request.method=="POST":
        util.save_entry(title, request.POST.get("content"))
        return redirect("title", title=title)

    return render(request, "edit.html", {"title":title, "content": util.get_entry(title)})

def create(request):
    if request.method=="POST":
        util.save_entry(request.POST.get('q'), request.POST.get('content'))
        return redirect("title", title=request.POST.get('q'))
    return render(request, "createnewpage.html")

def search(request):
    if request.method=="POST":
        if util.get_entry(request.POST.get('q')):
            return redirect("title", title=q)
        matches = [entry for entry in util.list_entries() if util.list_entries.lower() in entry.lower()]

        return render(request, "search.html", {
        "title": request.POST.get('q'),
        "matches": matches
    })


def randomi(request):
    return redirect("title", title=random.choice(util.list_entries()))

