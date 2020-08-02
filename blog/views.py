from django.shortcuts import render
from .models import Post

# posts = [
#     #dict inside list
#     {
#         'author': 'upasana',
#         'title': 'blog post',
#         'content': 'first post content',
#         'date_posted': 'today'
#     },
#
#     {
#         'author': 'gitu',
#         'title': 'blog post 2',
#         'content': 'second post content',
#         'date_posted': 'yesterday'
#     }
#
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

