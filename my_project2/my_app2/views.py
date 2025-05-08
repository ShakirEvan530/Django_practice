from django.shortcuts import render

def learning_django(req):
    return render(req,'my_app2/django.html')


def learning_api(req):
    return render(req,'my_app2/fastapi.html')