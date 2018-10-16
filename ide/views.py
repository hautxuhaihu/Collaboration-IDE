from django.shortcuts import render
from dashboard.models import Project

def ide(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'ide/ide.html', {'project':project})
