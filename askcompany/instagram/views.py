
from re import L
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpRequest , Http404
from django.shortcuts import render ,get_object_or_404
from .models import Post
from django.views.generic import ListView ,DetailView ,ArchiveIndexView, YearArchiveView

@method_decorator(login_required , name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10
post_list = PostListView.as_view()

# post_list = login_required(ListView.as_view(model= Post, paginate_by = 10))

# @login_required
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

post_archvie = ArchiveIndexView.as_view(model=Post ,date_field ='created_at', paginate_by=10)
post_archive_year = YearArchiveView.as_view(model=Post,date_field='created_at', make_object_list=True)


# def archives_year(request ,year):
#     return HttpResponse(f"{year}")