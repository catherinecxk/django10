from django.shortcuts import render

# Create your views here.
def blog(request):
    blogs = Blog.objects.all
    return render(request, 'blog/blog.html', {"blogs":blogs})
