from django.shortcuts import render, redirect
from .models import Student
from .form import Student_form

# Create your views here.

def  home(request):
    student_list = Student.objects.all()
    diction ={
        'title': "Home",'student_list': student_list
    }

    return render(request, 'first_app/index.html', context=diction)

def student_form(request):
    student_form = Student_form()
    if request.method == 'POST':
        student_form = Student_form(request.POST)
        if student_form.is_valid():
            student_form.save(commit=True)
            return redirect('home')

    diction = {
        'form': student_form, 'title': "Student Form"
    }
    return render(request, 'first_app/student_form.html', context= diction)

def student_info(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    diction ={
        'title': "Student Info", 'info': student_info,
    }
    return render(request, 'first_app/student_info.html', context= diction)

def student_update(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    student_form = Student_form(instance=student_info)
    if request.method == 'POST':
        student_form = Student_form(request.POST, instance=student_info)
        if student_form.is_valid:
            student_form.save()
            return redirect('home')
    diction={
        "title": "Student Update", "form": student_form,
    }
    return render(request, 'first_app/student_update.html', context=diction)

def student_delete(request, student_id):
    student_info = Student.objects.get(pk=student_id).delete()
    diction={
        
    }
    return render(request, 'first_app/student_delete.html', context=diction)
    
    