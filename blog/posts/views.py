from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return HttpResponse("<h1>Post List</h1>")

def post_create(request):
    return HttpResponse("<h1>Create</h1>")
