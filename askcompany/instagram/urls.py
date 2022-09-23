from django.urls import path ,re_path ,register_converter
from . import views



class YearConverter:
    regex = r"20\d{2}"

    def to_python(self,value):
        return int(value)
    def to_url(self,value):
        return str(value)

register_converter(YearConverter , 'year')
app_name = 'instagram'
urlpatterns = [
    path('',views.post_list),
    path('<int:pk>/',views.post_detail),
    # path('archives/<int:year>/', views.archives_year)
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year)
    path('archives/<year:year>/', views.archives_year),
]

#추가했어
#ddd
##dd