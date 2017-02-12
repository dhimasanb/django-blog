from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request): #list items
    queryset = Post.objects.all()
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

    return render(request, "posts/index.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
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
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "posts/form.html", context)

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
