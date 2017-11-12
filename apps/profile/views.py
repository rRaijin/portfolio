from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView
from apps.profile.models import *


class MainPage(TemplateView):
    template_name = 'main.html'


"""В ф-ии ниже воспользовался словарем вместо locals()"""

def profile(request, id):
    my_user = get_object_or_404(Profile, user_name_id=id)
    locality = Locality.objects.filter(human=my_user)
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


"""Главные пользовательские настройки, ф-я удаления не реализована за ненадобностью"""

class EditProfile(UpdateView):
    model = Profile
    fields = [
        'user_name', 'last_name', 'job', 'age', 'photo', 'email', 'website', 'phone', 'statement', 'interests'
    ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.id})

"""переделывать таблицу надо, полностью не верна"""
# class EditSkill(UpdateView):
#     model = DesignSkills
#     fields = []

""" Users administration options for add/refactor/del Language-skills"""

class AddLang(CreateView):
    model = LanguageSkills
    fields = [ 'human', 'language', 'qualification', 'level' ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

class EditLang(UpdateView):
    model = LanguageSkills
    fields = [ 'human', 'language', 'qualification', 'level' ]
    template_name = "user-self-configuration.html"
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        obj = LanguageSkills.objects.get(pk = self.kwargs['id'])
        return obj


class DeleteLang(DeleteView):
    model = LanguageSkills

    def get_object(self, queryset=None):
        obj = LanguageSkills.objects.get(pk = self.kwargs['id'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.human.id})

""""""
class AddRef(CreateView):
    model = Refereances
    fields = [ 'human', 'director', 'company', 'phone', 'email' ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

class EditRef(UpdateView):
    model = Refereances
    fields = ['human', 'director', 'company', 'phone', 'email']
    template_name = "user-self-configuration.html"
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        obj = Refereances.objects.get(pk = self.kwargs['id'])
        return obj


class DeleteRef(DeleteView):
    model = Refereances

    def get_object(self, queryset=None):
        obj = Refereances.objects.get(pk = self.kwargs['id'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.human.id})

""""""
class AddWorkExperience(CreateView):
    model = WorkExperience
    fields = [ 'human', 'organization', 'position', 'work_start', 'work_end', 'description' ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

class EditWorkExperience(UpdateView):
    model = WorkExperience
    fields = ['human', 'organization', 'position', 'work_start', 'work_end', 'description']
    template_name = "user-self-configuration.html"
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        obj = WorkExperience.objects.get(pk = self.kwargs['id'])
        return obj


class DeleteWorkExperience(DeleteView):
    model = WorkExperience

    def get_object(self, queryset=None):
        obj = WorkExperience.objects.get(pk = self.kwargs['id'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.human.id})

""""""
class AddEducation(CreateView):
    model = EducationQualifications
    fields = [ 'human', 'education', 'school', 'study_start', 'study_end', 'some_text' ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

class EditEducation(UpdateView):
    model = EducationQualifications
    fields = ['human', 'organization', 'position', 'work_start', 'work_end', 'description']
    template_name = "user-self-configuration.html"
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        obj = EducationQualifications.objects.get(pk = self.kwargs['id'])
        return obj


class DeleteEducation(DeleteView):
    model = WorkExperience

    def get_object(self, queryset=None):
        obj = EducationQualifications.objects.get(pk = self.kwargs['id'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.human.id})

""""""
class AddOther(CreateView):
    model = OtherQualifications
    fields = [ 'human', 'qualification', 'web_sourse', 'some_start', 'some_end', 'some_text' ]
    template_name = "user-self-configuration.html"

    def get_object(self, queryset=None):
        obj = Profile.objects.get(pk = self.kwargs['id'])
        return obj

class EditOther(UpdateView):
    model = OtherQualifications
    fields = [ 'human', 'qualification', 'web_sourse', 'some_start', 'some_end', 'some_text' ]
    template_name = "user-self-configuration.html"
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        obj = OtherQualifications.objects.get(pk = self.kwargs['id'])
        return obj


class DeleteOther(DeleteView):
    model = OtherQualifications

    def get_object(self, queryset=None):
        obj = OtherQualifications.objects.get(pk = self.kwargs['id'])
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("user_profile", kwargs={'id': self.object.human.id})