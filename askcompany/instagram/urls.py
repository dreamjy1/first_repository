from django.urls import path ,re_path ,register_converter
from . import views
from .converters import DayConverter, MonthConverter, YearConverter


register_converter(MonthConverter, 'month')
register_converter(YearConverter , 'year')
register_converter(DayConverter , 'day')

app_name = 'instagram'

urlpatterns = [
    path('archive/<year:year>/', views.post_archive_year, name='post_archives_year'),
    
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_day, name='post_archive_day'),
    
    path('archive/', views.post_archvie, name='post_archvie'),

    path('', views.post_list ),
    path('<int:pk>/',views.post_detail),
    # path('archives/<int:year>/', views.archives_year)
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year)
    # path('archives/<year:year>/', views.archives_year),
]

#추가했어
#ddd
##dd