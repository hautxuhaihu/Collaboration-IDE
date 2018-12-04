from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Project
from accounts.models import Contributor
from ide.views import ide
from random_key import id_generator, firebaseid_generator

@login_required(login_url='/')
def home(request):
    try:
        contributor = Contributor.objects.all().filter(user=request.user)
        yourprojects = Project.objects.all().filter(Developers__in=contributor)
        print(yourprojects)
    except:
        yourprojects = None

    try:
        ownprojects = Project.objects.all().filter(Owner=request.user)
        print(request.user)
    except:
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

def joinproject(request):
    if request.method=='POST':
        key = request.POST.get('key')

        print(key)
        try:
            project = Project.objects.filter(Key=key)[0]
        except:
            project = None

        print(project)

        if project is not None:
            contributor = Contributor(user=request.user)
            if Contributor.objects.filter(user=request.user):
                contributor = Contributor.objects.filter(user=request.user)[0]
                project.Developers.add(contributor)
            else:
                contributor.save()
                project.Developers.add(contributor)


            return redirect('ide', project.id)

        else:
            return HttpResponse("Invalid Key")

def createproject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        key = id_generator()

        while Project.objects.filter(Key=key):
            key = id_generator()

        firebasekey = firebaseid_generator()

        while Project.objects.filter(FirebaseID=key):
            firebasekey = firebaseid_generator()

        owner = request.user

        project = Project(Title=title, Description=description, FirebaseID=firebasekey, Key=key, Owner=owner)
        project.save()

        contributor = Contributor(user=request.user)
        if Contributor.objects.filter(user=request.user):
            contributor = Contributor.objects.filter(user=request.user)[0]
            project.Developers.add(contributor)
        else:
            contributor.save()
            project.Developers.add(contributor)

        return redirect('home')


