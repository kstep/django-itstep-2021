from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from app.models import Student
from datetime import date


# Create your views here.

def create_student(request):
    student = Student(
        name="John",
        group=1,
        birthday=date(year=1990,
                      month=4, day=15),
    )
    student.save()
    return HttpResponse(
        f"Created student id={student.pk}")

def show_students(request):
    students = Student.objects.all()
    return render(request,
                  "show_students.html",
                  {'students': students})


def length(request: HttpRequest):
    if 'str' in request.GET:
        query = request.GET["str"]
        return HttpResponse(f"{len(query)}")
    else:
        return HttpResponse('No input string')




