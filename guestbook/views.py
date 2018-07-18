from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook


def guestbook(request):
    guestbook_list = Guestbook.objects.all().order_by('-datetime')
    data = {'guestbook_list': guestbook_list}

    return render(request, 'guestbook/list.html', data)


def insert(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.content = request.POST['content']
    guestbook.password = request.POST['password']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    id = request.GET['id']
    data = {'guetbook_id': id}

    return render(request, 'guestbook/deleteform.html', data)


def delete(request):
    result = Guestbook.objects.\
        filter(id=request.POST['id']).\
        filter(password=request.POST['password'])

    if len(result) == 0:
        return HttpResponseRedirect('/guestbook/deleteform?id='+str(request.POST['id']))

    result.delete()

    return HttpResponseRedirect('/guestbook')