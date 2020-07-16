from django.shortcuts import render
from django.contrib import auth
# Create your views here.


def home(request):
	return render(request , 'books/index.html')


def dashboard(request):
	pass

def admindashboard(request):
	user = request.user



def login(request):
	if request.method =='POST':
		uname = request.POST['username']
		password = request.POST['password']
		print(uname,password)
		user = auth.authenticate(username=uname , password = password)
		if user is not None:
			if user.is_superuser:
				auth.login(request,user)
				return render(request , 'books/admindashboard.html')
			else:
				return render(request , 'books/dashboard.html')
	return render(request , 'books/login.html')

def logout(request):
	pass



def borrow_book(request):
	pass

def return_book(request):
	pass