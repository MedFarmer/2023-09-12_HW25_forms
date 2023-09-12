from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, FormView
from .models import Student, User
from .forms import StudentForm
from django.urls import reverse_lazy
from django.forms import ModelForm, PasswordInput, DateField

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

class StudentCreate(FormView):
    template_name = 'add.html'
    form_class = StudentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        grade = form.cleaned_data['grade']
        adding = Student(name=name, grade=grade)
        adding.save()

        return super().form_valid(form)

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



