from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from apps.profile.models import *


class MainPage(TemplateView):
    template_name = 'main.html'


"""В ф-ии ниже воспользовался словарем вместо locals(), т.к. с locals() при написании тестов могут быть проблемы"""

def profile(request, id):
    my_user = get_object_or_404(Profile, user_name_id=id)
    locality = get_object_or_404(Locality, human=my_user)
    design_skills = DesignSkills.objects.filter(human=my_user)
    languages = LanguageSkills.objects.filter(human=my_user)
    interests = Interest.objects.filter(profile=my_user)
    refereances = Refereances.objects.filter(human=my_user)
    experience = WorkExperience.objects.filter(human=my_user)
    education = EducationQualifications.objects.filter(human=my_user)
    other = OtherQualifications.objects.filter(human=my_user)
    context = {
        "user": my_user,
        "locality": locality,
        "design_skills": design_skills,
        "languages": languages,
        "interests": interests,
        "refereances": refereances,
        "experience": experience,
        "education": education,
        "other": other
    }
    return render(request, 'profiles/profile.html', context)