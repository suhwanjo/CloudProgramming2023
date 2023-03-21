from django.shortcuts import render
from .models import Post
# 매개변수랑 render에 첫번째 인자는 request 외워
def index(request):
    posts=Post.objects.all().order_by('-pk')
    # '-'는 내림차순
    return render(request,'blog/index.html',{'posts': posts})
# posts로 넘겨주는 것 까지가 백엔드의 의무
