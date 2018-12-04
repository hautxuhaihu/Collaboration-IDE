from django.shortcuts import render
from dashboard.models import Project
from ide.models import Chat
from django.http import JsonResponse

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
        project = Project.objects.get(pk=pk)
        messages = Chat.objects.filter(RefProject=project)

        return render(request, 'ide/ide.html', {'project':project, 'Chat':messages})

def Messages(request, pk):
    project = Project.objects.get(pk=pk)
    messages = Chat.objects.filter(RefProject=project)

    return render(request, 'ide/messages.html', {'project': project, 'Chat': messages})
