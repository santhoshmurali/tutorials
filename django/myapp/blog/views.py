from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post, AboutUS
from django.core.paginator import Paginator
from .forms import ContactForm

class VariablesMethods:
    def __init__(self, Title) -> None:
        self.__Title = Title

    @property
    def Title(self):
        return self.__Title
    
    @Title.setter
    def Title(self, value):
        if isinstance(value,str) and len(value)>0:
            self.__Title = value
        else:
            raise ValueError("The Title is not Valid")

vars = VariablesMethods("JVL Latest Post")

# Static Demo Data
# posts = [
# {'id':1,'title':'Post 1','content': 'Content of post 1'},
# {'id':2,'title':'Post 2','content': 'Content of post 2'},
# {'id':3,'title':'Post 3','content': 'Content of post 3'},
# {'id':4,'title':'Post 4','content': 'Content of post 4'},
# ]

# Create your views here.
def index(request):
    all_posts = Post.objects.all()

    #pagination
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blog/index.html',{'blog_title':vars.Title,'page_obj':page_obj})


def detail(request,slug):
    # Getting Static Data
    # post = next((item for item in posts if item['id']==int(post_id)),None)
    #post = [item for item in posts if item['id']==int(post_id)]
    try:
    # getting data from model id
        post = Post.objects.get(slug=slug)
        related_post = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not exist")
    

    return render(request,'blog/detail.html',{'post':post,'related_posts':related_post})


def old_url_view(request):
    #return redirect(reverse('blog:new_url_path'))
    return redirect(reverse('blog:new_url_path',kwargs={'post_id':34}))

def new_url_view(request,post_id):
    return HttpResponse(f"This is redirected from old url carried the post_id of {post_id}")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f"post data is {form.cleaned_data['name']} , {form.cleaned_data['email']} , {form.cleaned_data['message']}")
            success_message = "Your Message is saved"
            return render(request,'blog/contact.html', {'form':form, 'success_message':success_message})
        else:
            logger.debug(f"Form validation Failed")
        return render(request,'blog/contact.html', {'form':form, 'name':name,'email':email, 'message':message})
    return render(request,'blog/contact.html')


def about_view(request):
    about_content = AboutUS.objects.first().content
    return render(request,'blog/about.html', {'about_content':about_content})