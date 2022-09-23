
from django.http import HttpResponse,HttpRequest , Http404
from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.views.generic import ListView ,DetailView


post_list = ListView.as_view(model= Post, paginate_by = 10)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q' , '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#         #insatagram/templates/instagram/post_list.html
#     return render(request,'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q,
    
#     })
post_detail = DetailView.as_view(model=Post)
# def post_detail(request : HttpRequest , pk :int):
#     post = get_object_or_404(Post,pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#     })


def archives_year(request ,year):
    return HttpResponse(f"{year}")