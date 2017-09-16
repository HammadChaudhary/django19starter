from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
# Create your views here.
# Function based views
from .models import Post


def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("title"))
		instance.save()
		# Message Success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, "Failed: Creation of Post")

# Bad Practice - Not recommended
	# if request.method == "POST":
	# 	print(request.POST.get("title"))
	# 	print(request.POST.get("content"))
		# title = request.POST.get("title")
		# content = request.POST.get("title")
		# Post.objects.create(title=title)
		# Post.objects.create(content=content)

	my_context_data = {
		"form": form,
	}
	return render(request, "post_form.html", my_context_data)

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
		queryset_list = Post.objects.all() #.order_by("-timestamp")
	# Namming convention for variable, context, context_data

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "abc"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	my_context_data = {
		"object_list": queryset,
		"title": "My List",
		"page_request_var": page_request_var
	}
	# return render(request, "index2.html", my_context_data)

	# else:
	# 	my_context_data = {
	# 	"title": "List"
	# }

	return render(request, "post_list.html", my_context_data)

def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)

	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("title"))
		instance.save()
		# Message Success
		messages.success(request, "<a href='#'>Item</a> xSuccessfully Updated", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	my_context_data = {
	"title": "Detail",
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", my_context_data)

def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")
