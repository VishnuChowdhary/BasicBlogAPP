from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# POST
def post_create(request):
    return HttpResponse("<h1>Create</h1>")

# GET
def post_detail(request):
    return HttpResponse("<h1>Get Details</h1>")

# GET
def post_list(request):
    queryset = Post.objects.all()

    context = {
        'object_list' :queryset,
    }
    return render(request, 'index.html', context)
    # return HttpResponse("<h1>Display List</h1>")

# UPDATE
def post_update(request):
    return HttpResponse("<h1>Update Data</h1>")

# DELETE
def post_delete(request):
    return HttpResponse("<h1>Delete Data</h1>")