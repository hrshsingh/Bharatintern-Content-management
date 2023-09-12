from django.shortcuts import render
from blogs.models import UserPost

# Create your views here.
def blog_home(request):
    return render (request,'base_foot.html')
def posts(request):
    if request.method=='POST':
        author=request.POST.get('author')
        content=request.POST.get('content')
        title=request.POST.get('title')
        br=UserPost(author=author,content=content,title=title)
        br.save()

    
    return render (request,'posting.html')
