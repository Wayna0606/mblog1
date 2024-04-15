from django.shortcuts import render,redirect # type: ignore
from datetime import datetime
from mysite.models import Post # type: ignore

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html",locals())

def showpost(request, slug):
    try:
        post = Post.odjects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
