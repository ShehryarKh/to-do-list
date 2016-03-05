from django.shortcuts import render, redirect
from todos.models import Todo
from todos.forms import TodoForm, UpdateTodoForm,UserForm,UserProfileForm
from django.shortcuts import get_object_or_404

# Create your views here.

def register(request):

	register = False

	if request.method =='GET':
		if request.user.is_authenticated():
			return render(request, "index.html",{})
		user_form = UserForm()
		profile = UserProfileForm()

		context={
			'user_form':user_form,
			'profile': UserProfileForm
		}

		return render(request,"register.html", context)

	if request.method=='POST':
		#grab the info from the form
		user_form = UserForm(data=request.POST)
		userprofileform = UserProfileForm(data=request.POST)

		if user_form.is_valid() and userprofileform.is_valid():
			#save to database
			user_form.save()
			user.set_password(user.password)
			user.save()

			#sort out UserProfile instance, set commit=False
			profile = userprofileform.save(commit=False)
			profile.user = user

			#save any provided fields from userprofile

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				# save UserProfile model instance

				profile.save()

				register = True
			else:
				print(user_form.errors, userprofileform.errors)
		else:

			context={
			"user_form":user_form,
			"userprofileform":userprofileform
			}
			return render(request,'index.html', context)
	else:
		return render(request,'index.html', context)





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




