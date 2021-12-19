from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,FormView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from eschool.models import Course
from django.views.generic.detail import DetailView


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail',args=[self.course.id])

class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])


# class StudentCourseDetailView(LoginRequiredMixin, DetailView):
#     model = Course
#     template_name = 'students/course/detail.html'

#     def get_queryset(self):
#         qs = super(StudentCourseDetailView, self).get_queryset()
#         return qs.filter(students__in=[self.request.user])

#     def get_context_data(self, **kwargs):
#         context = super(StudentCourseDetailView,self).get_context_data(**kwargs)
#         # get course object
#         course = self.get_object()
#         if 'module_id' in self.kwargs:
#             # get current module
#             context['module'] = course.modules.get(id=self.kwargs['module_id'])
#         else:
#             # get first module
#             context['module'] = course.modules.all()[0]
#         return context

class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView,self).get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
            return context