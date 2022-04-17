from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from rest_framework.renderers import AdminRenderer, JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer, \
    SchemaJSRenderer, CoreJSONRenderer
from rest_framework.response import Response

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer


class EditStudentMixin:
    model = Student
    form_class = StudentForm


class ShowStudentMixin:
    queryset = Student.objects.select_related('group')


class AdaptiveTemplateRenderer(TemplateHTMLRenderer):
    def get_template_names(self, response, view):
        template_attr_name = '{}_template_name'.format(view.action)
        return ([getattr(view, template_attr_name)]
                if hasattr(view, template_attr_name) else
                super().get_template_names(response, view))

    def get_template_context(self, data, renderer_context):
        if isinstance(data, list):
            data = {'objects': data}
        return super().get_template_context(data, renderer_context)


class StudentViewSet(ModelViewSet):
    class StudentPagination(PageNumberPagination):
        page_size = 5
        max_page_size = 10

    pagination_class = StudentPagination
    renderer_classes = [
        JSONRenderer,
        AdminRenderer,
        BrowsableAPIRenderer,
        SchemaJSRenderer,
        CoreJSONRenderer,
        AdaptiveTemplateRenderer,
    ]
    serializer_class = StudentSerializer
    queryset = Student.objects.select_related('group')

    retrieve_template_name = 'students/student_detail.html'
    list_template_name = 'students/student_list.html'

    def list(self, request, *args, **kwargs):
        return Response(data=StudentSerializer(self.queryset.filter(first_name="nn"), many=True).data)


def show_students_view(request):
    page_num = request.GET.get('page', 1)
    queryset = Student.objects.all().order_by('first_name', 'last_name')
    paginator = Paginator(queryset, 5)
    page = paginator.get_page(page_num)

    # page = Paginator(Student.objects.all(), 5).get_page(page_num)

    return render(request, 'students/list.html', {
        'page_obj': page
    })


class ShowStudentsView(ShowStudentMixin, ListView):
    pass


class ShowStudentView(ShowStudentMixin, DetailView):
    pass


class EditStudentView(PermissionRequiredMixin, EditStudentMixin, UpdateView):
    permission_required = 'students.change_student'


class CreateStudentView(PermissionRequiredMixin, EditStudentMixin, CreateView):
    permission_required = 'students.add_student'
