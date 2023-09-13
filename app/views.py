
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy
from django.forms import ModelForm, PasswordInput, DateField
from django import forms

class StudentList(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'
    ordering = 'id'
    paginate_by = 5

    def get_queryset(self):
        data = Student.objects.all()
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = context['page_obj']
        return context     

class StudentDetails(DetailView):
    model = Student
    template_name = 'detail.html'
    context_object_name = 'student_details'
    pk_url_kwarg = 'id'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'name'    

class StudentUpdate(UpdateView):
    model = Student
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'grade']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'password')

        widgets = {
            'password':PasswordInput()
        }

class Signup(CreateView):
    form_class = UserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'lastname', 'grade')

class StudentCreate(CreateView):
    form_class = StudentForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')    




