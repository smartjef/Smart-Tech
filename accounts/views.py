from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView,FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Count
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from .models import Contact, Subscribe, main_app_details, Site_Contacts, user_profile
# Create your views here.

def index(request):
    return render(request, 'accounts/home.html')

class ProfileView(LoginRequiredMixin, TemplateView):
   template_name = 'accounts/profile.html'
   

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = UserProfileInfoForm
    template_name = 'accounts/profile_update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = UserProfileInfoForm(post_data, file_data, instance=request.user.user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile was successfully updated! ')
            return HttpResponseRedirect(reverse_lazy('profile'))
        context = self.get_context_data(
            user_form = user_form,
            profile_form = profile_form
        )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
         
def settings(request):
    teachers = user_profile.objects.filter(user_type='teacher').count()
    students = user_profile.objects.filter(user_type='student').count()
    parents = user_profile.objects.filter(user_type='parent').count()
    bloggers = user_profile.objects.filter(user_type='blogger').count() 
    developers = user_profile.objects.filter(user_type='developer').count()
    designers = user_profile.objects.filter(user_type='designer').count()
    analysts = user_profile.objects.filter(user_type='analyst').count() 
    context = {
        'teachers':teachers,
        'students':students, 
        'parents':parents,
        'bloggers':bloggers,
        'developers':developers,
        'designers':designers,
        'analysts':analysts,
        }
    messages.success(request, 'Welcome to your shorcuts  ')
    return render(request, 'accounts/settings.html', context)

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'accounts/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base = main_app_details.objects.all()
        context['base'] = base
        return context


class SubscribeView(CreateView):
    model = Subscribe
    fields = '__all__'
    template_name = 'accounts/subscribe.html'

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class ServiceView(TemplateView):
    template_name = 'accounts/service.html'