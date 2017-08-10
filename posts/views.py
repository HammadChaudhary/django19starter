from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
# Function based views
from .models import Post


def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request, id=None):
	# instance = Post.objects.get(id=2)
	instance = get_object_or_404(Post, id=id)
	# instance = get_object_or_404(Post, title="sdfasd")
	my_context_data = {
	"title": "Detail",
	"instance": instance
	}
	return render(request, "post_detail.html", my_context_data)

def post_list(request):

	# queryset = Post.objects.all()
	# 	# Namming convention for variable, context, context_data
	# my_context_data = {
	# 	"object_list": queryset,
	# 	"title": "User List"
	# }
	
	if request.user.is_authenticated():
		queryset = Post.objects.all()
		# Namming convention for variable, context, context_data
		my_context_data = {
		"object_list": queryset,
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
