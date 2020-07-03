from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from .forms import CreateNewList

# Create your views here.
def HomeView(request : HttpRequest):
    return render(request, "home.html")


def ListView(request : HttpRequest, id):
    tdl = ToDoList.objects.get(id=id)
    print(request.method)
    print(request.GET)
    print(request.POST)
    if request.method == "POST":
        print(request.POST)
    
        if request.POST.get("save"):
    
            for item in tdl.item_set.all():
    
                if request.POST.get(f"c{item.id}") == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
    
        elif request.POST.get("new"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                tdl.item_set.create(text=txt, complete=False)
            else:
                print("Invalid item")

    return render(request, "list.html", {"tdl":tdl})


def CreateView(request : HttpRequest):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            tdl = ToDoList(name=name)
            tdl.save()
            request.user.todolist.add(tdl)
        return HttpResponseRedirect("/%i"%(tdl.id))
    else:
        form = CreateNewList()
    return render(request, "create.html", {"form":form})

def View(request: HttpRequest):
    return render(request, "view.html", {})