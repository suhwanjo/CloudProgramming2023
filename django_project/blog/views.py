from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
# 매개변수랑 render에 첫번째 인자는 request 외워

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# 정적 FBV
#def index(request):
#    posts = Post.Objects.all()
#    return render(request,'blog/index.html'{'posts':posts})
#
#def single_post_page(request,post_num):
#    post=Post.objects.get(pk=post_num)
#    return render(request, 'blog/post_detail.html', {'post':post})
# 먼저 url 패턴에 잘 걸리는지 확인하고 함수 작성