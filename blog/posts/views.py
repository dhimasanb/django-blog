from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request): #list items
    queryset_list = Post.objects.all() # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 5 post per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
        "title": "List"
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }

    return render(request, "posts/list.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # if request.method == "POST":
    #     print "title" + request.POST.get("content")
    #     print request.POST.get("title")
    context = {
        "form": form,
    }
    return render(request, "posts/form.html", context)

def post_detail(request, id=None): #retrieve
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "posts/detail.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "posts/form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:index")
