from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView,DetailView
# 매개변수랑 render에 첫번째 인자는 request 외워


class PostList(ListView):
    model = Post
    ordering = '-pk'

    # 오버라이드
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def categories_page(request,slug):
    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context={
        'category': category,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_post_count': Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context={
        'tag': tag,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_post_count': Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)

# 정적 FBV
#def index(request):
#    posts = Post.Objects.all()
#    return render(request,'blog/index.html'{'posts':posts})
#
#def single_post_page(request,post_num):
#    post=Post.objects.get(pk=post_num)
#    return render(request, 'blog/post_detail.html', {'post':post})
# 먼저 url 패턴에 잘 걸리는지 확인하고 함수 작성