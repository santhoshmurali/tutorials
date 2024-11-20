from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'blog\index.html')


def detail(request,post_id):
    return render(request,'blog\detail.html')


def old_url_view(request):
    #return redirect(reverse('blog:new_url_path'))
    return redirect(reverse('blog:new_url_path',kwargs={'post_id':34}))

def new_url_view(request,post_id):
    return HttpResponse(f"This is redirected from old url carried the post_id of {post_id}")