from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Project
from accounts.models import Contributor

@login_required(login_url='/')
def home(request):
    try:
        contributor = Contributor.objects.all().filter(user=request.user)
        yourprojects = Project.objects.all().filter(Developers__in=contributor)
        ownprojects = Projects.objects.all().filter(Owner__exact=request.user)
    except:
        yourprojects = None
        ownprojects = None

    try:
        recent = Project.objects.order_by('Created')[:5]
    except:
        recent = Project.objects.all().filter('Created')[:5]

    context = {
        'yourprojects':yourprojects,
        'ownprojects':ownprojects,
        'recent':recent,
    }

    return render(request, 'dashboard/home.html',context)

def join(request):
    if request.method=='POST':
        key = request.POST.get('key')

        try:
            project = Project.objects.filter(Key=key)[0]
        except:
            print('No such object')
            project = None

        if project is not None:
            contributor = Contributor(user=request.user)
            contributor.save()

            project.Developers.add(contributor)

            return render(request, 'ide/ide.html', {'project':project})

