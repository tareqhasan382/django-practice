from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    data = [
            {
                'id': 1,
                'name': 'John Doe',
                'age': 21,
                'course': 'Computer Science'
            },
            {
                'id': 2,
                'name': 'Jane Smith',
                'age': 22,
                'course': 'Information Technology'
            },
            {
                'id': 3,
                'name': 'Alice Johnson',
                'age': 20,
                'course': 'Mechanical Engineering'
            }
    ]
    return HttpResponse(data)