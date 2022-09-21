from msilib.schema import ListView
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render 
from .models import Post
from django.views.generic import ListView

post_list = ListView.as_view(model= Post)

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
def post_detail(request : HttpRequest,pk :int):
    response = HttpResponse()
    response.write("hello world");
    return response
# Create your views here.
