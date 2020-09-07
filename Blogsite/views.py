from django.shortcuts import render, redirect
from .models import BlogUser, Blog, Contact
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BlogEditForm, NewBlogForm


@login_required(login_url='/login')
def home(request):
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.all().order_by('-id')[:1000]
    context = {
        'user': user,
        'blog': blog,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def about(request):
    user = BlogUser.objects.get(user=request.user)
    context = {
        'user': user,
    }
    return render(request, 'about.html', context)


@login_required(login_url='/login')
def contact(request):
    user = BlogUser.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, contact_no=contact_no, message=message)
    context = {
        'user': user,
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/login')
def post(request, pk):
    blogs = Blog.objects.all()
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.get(id=pk)
    blogger = Blog.objects.get(id=pk)
    blogger.views.add(user)
    views = blogger.views.count()
    if request.method == 'POST':
        if 'likes' in request.POST:
            likes = request.POST['likes']
            blogss = Blog.objects.get(id=pk)
            if user in blog.likes.filter(user=request.user):
                blogss.likes.remove(user)
            else:
                blogss.likes.add(user)
    if user in blog.likes.filter(user=request.user):
        x = True
    else:
        x = False
    likes = blogger.likes.count()
    context = {
        'x': x,
        'user': user,
        'likes': likes,
        'blog': blog,
        'blogs': blogs,
        'views': views,
    }
    return render(request, 'post.html', context)


@login_required(login_url='/login')
def new_post(request):
    form = NewBlogForm()
    user = BlogUser.objects.get(user=request.user)
    if request.method == 'POST':
        userss = request.user
        users = BlogUser.objects.get(user=userss)
        form = NewBlogForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['blog']
            title = form.cleaned_data['heading']
            user = users
            Blog.objects.create(blog=content, user=user, heading=title)
        return redirect('/')
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'New Post.html', context)


@login_required(login_url='/login')
def my_blogs(request):
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.filter(user=user)
    context = {
        'user': user,
        'blog': blog,
    }
    return render(request, 'my_blog.html', context)


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password-repeat']:
            try:
                user = User.objects.get(username=request.POST['username'], email=request.POST['email'])
                return render(request, 'register.html', {'error': 'Username Taken'})

            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=request.POST['email'])
                    return render(request, 'register.html', {'error': 'Email Already Taken'})

                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['username'],
                                                    password=request.POST['password'],
                                                    email=request.POST['email'])
                name = request.POST['name']
                username = request.POST['username']
                email = request.POST['email']
                users = BlogUser(user=user, full_name=name, email=email, username=username)
                users.save()
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'register.html', {'error': 'Password dosent match'})
    else:
        return render(request, 'register.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def delete(request, pk):
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('/my/blogs/')
    context = {
        'user': user,
        'blog': blog,
    }
    return render(request, 'delete.html', context)


@login_required(login_url='/login')
def edit(request, pk):
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.get(id=pk)
    form = BlogEditForm(instance=blog)
    if request.method == 'POST':
        form = BlogEditForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'edit.html', context)


def profile(request, pk):
    blogger = BlogUser.objects.get(id=pk)
    if request.method == 'POST':
        followers = blogger.followers.filter(id=pk)
        if blogger.followers.filter(id=request.user.id).exists():
            blogger.followers.remove(request.user)
        else:
            blogger.followers.add(request.user)
    if blogger.followers.filter(id=request.user.id).exists():
        x = True
    else:
        x = False
    followers = blogger.followers.count()
    BlogCount = Blog.objects.filter(user_id=pk).count()
    blogs = Blog.objects.filter(user_id=pk)

    context = {
        'blogs': blogs,
        'blogcount': BlogCount,
        'followers': followers,
        'x': x,
        'user': blogger,
    }
    return render(request, 'profile.html', context)