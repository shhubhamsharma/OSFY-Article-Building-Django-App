from django.shortcuts import render

from django.template import loader, Context
from django.http import HttpResponse
from CMS.models import IntroductionPage

def archive(request):
    contents=IntroductionPage.objects.all()
    t=loader.get_template("archive.html")
    c=Context({'contents':contents})
    return HttpResponse(t.render(c))
