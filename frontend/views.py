from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    abt = Biography.objects.all()[:3]
    pst = Post.objects.order_by('-created')[:3]
    context = {
        'about':abt,
        'post':pst
    }
    return render(request, 'frontend/index.html', context)


def detail_index(request, home_id):
    detail = Biography.objects.get(id=index_id)
    return render(request, 'frontend/detail.html', {'index_detail':detail})
