from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based views

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	my_context_data = {
	"title": "Detail"
	}
	return render(request, "index.html", my_context_data)

def post_list(request):
	if request.user.is_authenticated():
		# Namming convention for variable, context, context_data
		my_context_data = {
		"title": "My User List"
	}
	# return render(request, "index2.html", my_context_data)

	else:
		my_context_data = {
		"title": "List"
	}

	return render(request, "index.html", my_context_data)

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
