from django.contrib.auth.mixins import PermissionRequiredMixin
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


class EditStudentView(PermissionRequiredMixin, EditStudentMixin, UpdateView):
    permission_required = 'students.change_student'


class CreateStudentView(PermissionRequiredMixin, EditStudentMixin, CreateView):
    permission_required = 'students.add_student'


