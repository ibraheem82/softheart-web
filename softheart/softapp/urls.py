from django.urls import path

from . views import  CoursesListView, about
urlpatterns = [
    path('', CoursesListView.as_view(), name='home'),
    # path('', views.home, name = 'home'),
    # path('about', views.about, name = 'about')
]
