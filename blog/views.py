from django.forms.models import fields_for_model
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import CommentForm
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.

def homepage_view(request):
  context = {
    'posts': BlogPost.objects.all()
  }
  return render(request, 'index.html', context)


def post_view(request, id):
  commentForm = CommentForm(request.POST or None)
  if commentForm.is_valid():
    commentForm.save()

  context = {
    'post': get_object_or_404(BlogPost, id=id),
    'commentForm': commentForm
  }
  return render(request, 'post.html', context)


def json_posts_view(request):
  posts = BlogPost.objects.all()
  json_posts = serialize('json', posts, fields=('title', 'preface', 'description'))
  return HttpResponse(json_posts, content_type="application/json")
