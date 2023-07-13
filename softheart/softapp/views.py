from django.views.generic import ListView
from django.shortcuts import render
from .models import Course, Category
# Create your views here.

# def courses_list(request):
#     courses = Course.objects.all()
#     context = {
#         'courses': courses
#     }
#     return render(request, 'softapp/index.html', context)
    
class CoursesListView(ListView):
    model = Course
    template_name = 'softapp/index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



def about(request):
  return render(request, 'softapp/about.html')