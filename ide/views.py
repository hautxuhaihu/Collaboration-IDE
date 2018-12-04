from django.shortcuts import render, HttpResponse
from dashboard.models import Project
from ide.models import Chat, Source, Directory, File
from django.http import JsonResponse
from random_key import firebaseid_generator

def ide(request, pk):

    if request.method == 'POST':
        msg = request.POST.get('message')
        user = request.user
        project = Project.objects.get(pk=pk)

        c = Chat(message=msg, username=user, RefProject=project)

        user = str(user)

        if msg!='':
            c.save()

        return JsonResponse({'msg': msg, 'user': user, 'id': pk})
    else:
        file = File.objects.get(pk=pk)

        print(file)

        project = file.SourceFolder.RefProject
        contributors = project.Developers.all()
        print(project)
        source = Source.objects.filter(RefProject=project)[0]
        messages = Chat.objects.filter(RefProject=project)
        directory = Directory.objects.filter(SourceFolder=source)
        files = File.objects.filter(SourceFolder=source)
        return render(request, 'ide/ide.html', {'project':project, 'Chat':messages,'file':file, 'files': files, 'directory':directory, 'contributors':contributors})

def Messages(request, pk):
    project = Project.objects.get(pk=pk)
    messages = Chat.objects.filter(RefProject=project)

    return render(request, 'ide/messages.html', {'project': project, 'Chat': messages})

def Overview(request, pk):
    project = Project.objects.get(pk=pk)
    contributors = project.Developers.all()

    print(contributors)

    source = Source.objects.filter(RefProject=project)[0]
    directory = Directory.objects.filter(SourceFolder=source)
    files = File.objects.filter(SourceFolder=source)

    return render(request, 'ide/projectoverview.html', {'project':project, 'directory':directory, 'files':files, 'contributors':contributors})

def CreateFile(request, pk):
    if request.method == 'POST':
        name = request.POST.get("name")
        language = request.POST.get("language")
        dir = request.POST.get("location")
        firebaseID = firebaseid_generator()
        project = Project.objects.get(pk=pk)

        source = Source.objects.filter(RefProject=project)[0]

        if dir[0]=='/':
            dir = dir[1:]

        locations = dir.split('/')

        file = File(Name=name, Language=language, FirbaseID=firebaseID, inSource=True, SourceFolder=source)

        file.save()

        contributors = project.Developers.all()

        directory = Directory.objects.filter(SourceFolder=source)
        files = File.objects.filter(SourceFolder=source)

        return render(request, 'ide/projectoverview.html',
                      {'project': project, 'directory': directory, 'files': files, 'contributors': contributors})
    else:
        return HttpResponse('<p>Some error occured!</p>')



