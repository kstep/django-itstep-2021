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

def hello(request: HttpRequest, a, b, c):
    """
    Solve square equation, requires
    a, b, and c in query-string.

    :param request:
    :return:
    """
    try:
        if a == 0:
            x1 = -c / b
            x2 = x1
        else:
            d = (b*b - 4*a*c) ** 0.5
            x1 = (-b + d) / 2*a
            x2 = (-b - d) / 2*a

        return render(request, "hello.txt", {
            'x1': x1,
            'x2': x2,
        })
    except KeyError:
        return HttpResponse("I need a, b, and c", status=400)
    except ValueError:
        return HttpResponse("I accept numbers only", status=400)
    except ZeroDivisionError:
        return HttpResponse("Both a and b can't be zero", status=400)




def length(request: HttpRequest):
    if 'str' in request.GET:
        query = request.GET["str"]
        return HttpResponse(f"{len(query)}")
    else:
        return HttpResponse('No input string')




