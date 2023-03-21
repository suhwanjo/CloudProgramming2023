from django.shortcuts import render
# 매개변수 request 외워
def index(request):
    return render(request,'blog/index.html')
