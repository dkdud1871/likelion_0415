from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request): # post를 전부 가져아서 템플릿에 가져다줌
    posts1 = Post.objects
    return render(request, 'blog/home.html', {'posts':posts1})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html',{'post': post_detail})
def post_delete(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect('home')
def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/new.html',{'form':form})        


def post_edit(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)

        if form.is_valid():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/new.html', {'form':form})