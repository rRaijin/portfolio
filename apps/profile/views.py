from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
# from apps.profile.models import UserProfile
from apps.profile.models import *


def landing(request, id=id):
    myuser = get_object_or_404(Profile, id=1)
    locality = get_object_or_404(Locality, human=myuser)
    lanskills = LanguageSkills.objects.filter(human=myuser)
    context = {
        "myuser": myuser,
        "locality": locality,
        "lanskills": lanskills,
    }
    return render(request, 'main.html', context)