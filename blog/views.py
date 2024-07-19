from django.shortcuts import render, get_object_or_404
from .models import post
from django.http import Http404

def post_list(request):
    posts = post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts' : posts})


def post_detail(request, id):
    post = get_object_or_404(post,
                             id=id,
                             status = post.Status.PUBLISHED)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post' : post})


