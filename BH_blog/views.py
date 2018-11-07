from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Plate,User,Reply,Post
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

# def home(request):
#     plates = Plate.objects.all()
#     return render(request,'home.html',{'plates':plates})

def get_index(request):
    plates = Plate.objects.all()
    return render(request,'BH_blog_templates/BH_blog_index.html',{'plates':plates})

def get_posts(request,id):
    plates = Plate.objects.all()
    if request.method=="GET":
        plate = Plate.objects.get(id=id)
        return render(request,'BH_blog_templates/BH_blog_posts.html',{'plate':plate,'plates':plates})

def index_login(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if next_url:
                return redirect(next_url)
            return redirect(to="index") #这里使用的"index"是url.py里面的[name=]
        return HttpResponseRedirect(request.get_full_path()) #登录失败，依旧跳转到当前页面
    return render(request, 'BH_blog_templates/BH_blog_login.html',{'next_url':next_url})

def index_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not User.objects.filter(username=username).exists():
            if password1==password2:
                user = User(username=username)
                user.set_password(password1)
                user.save()
                messages.success(request, "注册成功")
                return redirect(to="login")
            else:
                messages.warning(request, "前后密码不一致")
        else:
            messages.warning(request, "账号已存在")
    return render(request, 'BH_blog_templates/BH_blog_register.html')

@login_required
def post_post(request,id):
    if request.method=="POST":
        plate = Plate.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content,users=request.user,column=plate)
        messages.success(request, "帖子新建成功")
    return redirect(to='plate',id=id)

def get_article(request,id):
    plates = Plate.objects.all()
    article = Post.objects.get(id=id)
    return render(request,'BH_blog_templates/BH_blog_article.html',{'article':article,'plates':plates})

@login_required
def post_article(request,id):
    plates = Plate.objects.all()
    if request.method=="POST":
        post = Post.objects.get(id=id)
        comment = request.POST.get('comment')
        reply = Reply.objects.create(user=request.user,post=post,content=comment)
        messages.success(request, "评论成功")
    return redirect(to='article',id=id)

def put_article(request,id):
    if request.method=="POST":
        article = Post.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        messages.success(request, "修改帖子成功")
    return redirect(to='article',id=id)

def delete_article(request,id):
    if request.method=="GET":
        article = Post.objects.get(id=id)
        column = article.column
        article.delete()
        messages.success(request, "帖子删除成功")
    return redirect(to='plate',id=column.id)

def delete_comment(request,id):
    if request.method=='GET':
        reply = Reply.objects.get(id=id)
        article = reply.post
        reply.delete()
        messages.success(request, "回复成功")
    return redirect(to='article',id=article.id)


