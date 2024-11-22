from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
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

posts = [
{'id':1,'title':'Post 1','content': 'Content of post 1'},
{'id':2,'title':'Post 2','content': 'Content of post 2'},
{'id':3,'title':'Post 3','content': 'Content of post 3'},
{'id':4,'title':'Post 4','content': 'Content of post 4'},
]

# Create your views here.
def index(request):
    # The belo code cannot be used as a global constant due to reverse whoch requires 'request' object. 
    # posts = [
    # {'id':1,'title':'Post 1','content': 'Content of post 1','url_path':reverse('blog:detail',kwargs={'post_id':1})},
    # {'id':2,'title':'Post 2','content': 'Content of post 2','url_path':reverse('blog:detail',kwargs={'post_id':2})},
    # {'id':3,'title':'Post 3','content': 'Content of post 3','url_path':reverse('blog:detail',kwargs={'post_id':3})},
    # {'id':4,'title':'Post 4','content': 'Content of post 4','url_path':reverse('blog:detail',kwargs={'post_id':4})},
    # ]
    return render(request,'blog\index.html',{'blog_title':vars.Title,'posts':posts})


def detail(request,post_id):
    post = next((item for item in posts if item['id']==int(post_id)),None)
    # logger = logging.getLogger("Testing")
    # logger.debug(f"post variable is {post}")
    return render(request,'blog/detail.html',{'blog_title':vars.Title})


def old_url_view(request):
    #return redirect(reverse('blog:new_url_path'))
    return redirect(reverse('blog:new_url_path',kwargs={'post_id':34}))

def new_url_view(request,post_id):
    return HttpResponse(f"This is redirected from old url carried the post_id of {post_id}")