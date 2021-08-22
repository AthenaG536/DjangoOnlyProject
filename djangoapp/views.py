from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from djangoapp.models import AccountHolder, Risk


def index(request):
    latest_accountholder_list = AccountHolder.objects.order_by('-date_of_birth')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_accountholder_list': latest_accountholder_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, username):
    return HttpResponse("You're looking at user details of %s." % username)

def risks(request, username):
    response = "You're looking at the risks created by %s."
    return HttpResponse(response % username)
