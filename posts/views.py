try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post, Genre

from django.contrib.auth.decorators import login_required

import random

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "create.html", context)


@login_required(login_url="/login/")
def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	

	if instance.publish > timezone.now().date() or instance.draft == 'YES':
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	genre  = Genre.objects.all()

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}

	context = {
		"genre":genre,
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post.html", context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	
	favourites_list = Post.objects.favourites()

	print (favourites_list)

	if favourites_list.count()< 5:
		 favourites_queryset_list = favourites_list
	else:
		favourites_queryset_list = random.sample(favourites_list,5)

	print favourites_queryset_list

	genre  = Genre.objects.all()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 4) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)

	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"genre":genre,
		"object_list": queryset, 
		"favourites" : favourites_queryset_list,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "index.html", context)


def post_list_genre(request, genre):
	today = timezone.now().date()
	genre = genre

	try:
		genre_id = Genre.objects.filter(title=genre)[0].id
		queryset_list = Post.objects.active().filter(genre=genre_id)
		genre  = Genre.objects.all()

	except:
		pass

	queryset_list = Post.objects.active()

	favourites_list = Post.objects.favourites()
	if favourites_list.count()< 5:
		 favourites_queryset_list = favourites_list
	else:
		favourites_queryset_list = random.sample(favourites_list,5)

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.filter(genre=genre_id)
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 3) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"genre":genre,
		"object_list": queryset,
		"favourites" : favourites_queryset_list, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "index.html", context)



def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "create.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
