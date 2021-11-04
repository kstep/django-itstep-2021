from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .models import Student
from .forms import StudentForm


class EditStudentMixin:
    model = Student
    form_class = StudentForm


class ShowStudentMixin:
    queryset = Student.objects.select_related('group')


class ShowStudentsView(ShowStudentMixin, ListView):
    pass


class ShowStudentView(ShowStudentMixin, DetailView):
    pass


class EditStudentView(EditStudentMixin, UpdateView):
    pass


class CreateStudentView(EditStudentMixin, CreateView):
    pass


