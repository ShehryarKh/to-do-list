from django.shortcuts import render, redirect
from todos.models import Todo
from todos.forms import TodoForm, UpdateTodoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
	all_todos = Todo.objects.all()

	context = {
		"todos": all_todos,
		"create_form":TodoForm()
	}

	return render(request, 'index.html', context)


def create(request):
	if request.method =="GET":

		context = {
			"form":TodoForm()
		}

		return render(request, "create.html", context)

	elif request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("todos:index")



def details(request,id):
	if request.method =="POST":
		task = get_object_or_404(Todo,pk=id)
		form = UpdateTodoForm(request.POST,instance = task)
		if form.is_valid():
			form.save()
			return redirect("todos:index")
	if request.method == "GET":
		task = get_object_or_404(Todo,pk=id)
		form = UpdateTodoForm(instance = task)
		context = {
			"todos":task,
			"form":form
		}
		return render (request, "details.html", context)


def delete(request,id):
	
	if request.method =="POST":
		task = get_object_or_404(Todo,pk=id)
		task.delete()
		return redirect("todos:index")
	return render (request, "index.html", {})




