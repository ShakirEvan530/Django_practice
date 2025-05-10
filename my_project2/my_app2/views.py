from django.shortcuts import render

def learning_django(req):
    coursename = {'cname':'Django 3.0'}
    return render(req,'my_app2/django.html',coursename)


def learning_api(req):
    course = {'cname':'FastApi', 'version':'3.25'}
    return render(req,'my_app2/fastapi.html',course)