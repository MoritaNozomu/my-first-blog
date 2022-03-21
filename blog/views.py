from django.shortcuts import render

# Create your views here.

from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})