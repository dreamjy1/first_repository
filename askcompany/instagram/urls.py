from django.urls import path ,re_path
from . import views

urlpatterns = [
    path('',views.post_list),
    path('<int:pk>/',views.post_detail),
    path('<str:pk>/',views.post_detail_2),
    
]

#추가했어
#ddd
##dd