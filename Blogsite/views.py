from django.shortcuts import render, redirect
from .models import BlogUser, Blog, Contact
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BlogEditForm, NewBlogForm


@login_required(login_url='/login')
def home(request):
    user = BlogUser.objects.all()
    blog = Blog.objects.all().order_by('-id')[:10]
    context = {
        'user': user,
        'blog': blog,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='/login')
def contact(request):
    user = BlogUser.objects.all()
    blog = Blog.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, contact_no=contact_no, message=message)
    context = {
        'user': user,
        'blog': blog,
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/login')
def post(request, pk, name):
    blogs = Blog.objects.all()
    user = BlogUser.objects.all()
    blog = Blog.objects.get(id=pk, heading=name)
    context = {
        'user': user,
        'blog': blog,
        'blogs': blogs,
    }
    return render(request, 'post.html', context)


@login_required(login_url='/login')
def new_post(request):
    form = NewBlogForm()
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
        'form': form
    }
    return render(request, 'New Post.html', context)


@login_required(login_url='/login')
def my_blogs(request):
    user = BlogUser.objects.get(user=request.user)
    blog = Blog.objects.filter(user=user)
    context = {
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
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('/my/blogs/')
    context = {
        'blog': blog,
    }
    return render(request, 'delete.html', context)


@login_required(login_url='/login')
def edit(request, pk):
    blogs = Blog.objects.all()
    blog = Blog.objects.get(id=pk)
    form = BlogEditForm(instance=blog)
    if request.method == 'POST':
        form = BlogEditForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'blogs': blogs,
    }
    return render(request, 'edit.html', context)
