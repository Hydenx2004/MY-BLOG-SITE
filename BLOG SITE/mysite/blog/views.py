from django.shortcuts import render, redirect
from blog.models import Blog
from blog.forms import BlogForm, BlogIdForm

def brand(request):
    return render(request, 'Brand.html')

def home(request):
    return render(request, "Home.html")

def create(request):
    if request.method == "POST":
        blog_form = BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('view')  # Redirect to the homepage after successful creation
    else:
        blog_form = BlogForm()
    return render(request, "Create.html", {'Blog_Form': blog_form})


def delete(request):
    if request.method == "POST":
        blog_id_form = BlogIdForm(request.POST)
        if blog_id_form.is_valid():
            blog_id = blog_id_form.cleaned_data['Blog_Id']
            try:
                blog = Blog.objects.get(Blog_Id=blog_id)
                blog.delete()
                return redirect('home')  # Redirect to the homepage after successful deletion
            except Blog.DoesNotExist:
                return render(request, "NotFound.html")
    else:
        blog_id_form = BlogIdForm()
    return render(request, 'delete.html', {'blog_id_form': blog_id_form})

def not_found(request):
    return render(request, "NotFound.html")

def view(request):
    blog_list = Blog.objects.all().order_by("-Date")
    blog_dict = {'Blogs': blog_list}
    return render(request, "view.html", context=blog_dict)
