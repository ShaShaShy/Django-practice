from django.shortcuts import render, redirect
from myApp.models import Users
from myApp.forms import userForm

# Create your views here.
def getUsers(request):
	myuser = Users.objects.all()
	return render(request, 'myApp/index.html', {'myuser':myuser})

def createUser(request):
	user_form = userForm()
	if request.method == 'POST':
		user_form = userForm(request.POST)
		if user_form.is_valid():
			user_form.save()
		return redirect('/')
	return render(request,'myApp/createUser.html', {'user_form':user_form})

def deleteUser(request, id):
	user = Users.objects.get(id=id)
	user.delete()
	return redirect('/')
