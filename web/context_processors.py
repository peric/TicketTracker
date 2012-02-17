import django
import sys

def django_version(request):
    return { 'django_version': django.get_version() }

def python_version(request):
    return { 'python_version': sys.version.split(' ')[0] }
