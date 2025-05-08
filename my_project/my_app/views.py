from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django_prac(req):
    return HttpResponse('Hello Evan How are you!!')

def machine_learning(req):
    return HttpResponse('this is about machine learning!!')

def deep_learning(req):
    return HttpResponse('this is about deep learning!!')


