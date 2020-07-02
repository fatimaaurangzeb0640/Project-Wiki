from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import re, random
from . import util
import markdown2
from markdown2 import markdown_path, Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if request.method == 'GET':
        titleEnc = title
    html = markdown2.markdown(util.get_entry(titleEnc))
    return render(request, "encyclopedia/entry.html", {
        "entry":  html,
        "title": titleEnc
    })

def search(request):
    entry = request.POST["q"]
    entries = util.list_entries()
    entryFound = ""
    entryList = []

    # To see if the user's entry is present
    for e in entries:
        if e == entry:
            entryFound = entry

    # If found the redirect to that page    
    if entryFound != "":
            return HttpResponseRedirect(reverse("entry", args=(entryFound,)))

    # If not then search for similar entries
    if entryFound == "":
            for e in entries:
               if re.search(entry, e):
                   entryList.append(e)
            return render(request, "encyclopedia/search.html", {
        "entries":  entryList
    })

def newentry(request):
    return render(request, "encyclopedia/newentry.html", {
    })

def saveentry(request):
    entrytitle = request.POST["entrytitle"]
    entrytext = request.POST["entrytext"]
    entries = util.list_entries()
    for entry in entries:
        if entry == entrytitle:
            return HttpResponseRedirect(reverse("error"))
    util.save_entry(entrytitle, entrytext)
    return HttpResponseRedirect(reverse("entry", args=(entrytitle,)))

def editentry(request, title):
    entrytext = util.get_entry(title)
    return render(request, "encyclopedia/editentry.html", {
            "title": title, 
            "entrytext": entrytext
        })

def error(request):
    return render(request, "encyclopedia/error.html", {
            "message": "Try again, this encyclopedia already exists."
            })

def saveeditentry(request, title):
    title = title
    entrytext = request.POST["entrytext"] 
    util.save_entry(title, entrytext)
    return HttpResponseRedirect(reverse("entry", args=(title,)))

def randompage(request):
    entries = util.list_entries()
    title = random.choice(entries)   
    return HttpResponseRedirect(reverse("entry",args=(title,)))         



    




