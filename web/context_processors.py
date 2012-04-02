import django
import sys
from web import models

def django_version(request):
    return { 'django_version': django.get_version() }

def python_version(request):
    return { 'python_version': sys.version.split(' ')[0] }

def unfinished_tickets_count(request):
    count = 0

    if request.user.is_authenticated():
        current_sprint_queryset = models.Sprint.objects.all().order_by('-date_ends')

        if current_sprint_queryset.count():
            count = models.Story.objects.filter(sprint=current_sprint_queryset[0], task__owner=request.user).exclude(state__in=['DONE', 'FIRE']).distinct().count()

    return { 'unfinished_tickets_count': count }
