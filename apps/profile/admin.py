from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [field.name for field in Profile._meta.fields]

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)


class LocalityAdmin(admin.ModelAdmin):
    model = Locality
    list_display = [field.name for field in Locality._meta.fields]

    class Meta:
        model = Locality

admin.site.register(Locality, LocalityAdmin)


class WorkExperienceAdmin(admin.ModelAdmin):
    model = WorkExperience
    list_display = [field.name for field in WorkExperience._meta.fields]

    class Meta:
        model = WorkExperience

admin.site.register(WorkExperience, WorkExperienceAdmin)


class EducationQualificationsAdmin(admin.ModelAdmin):
    model = EducationQualifications
    list_display = [field.name for field in EducationQualifications._meta.fields]

    class Meta:
        model = EducationQualifications

admin.site.register(EducationQualifications, EducationQualificationsAdmin)


class DesignSkillsAdmin(admin.ModelAdmin):
    model = DesignSkills
    list_display = [field.name for field in DesignSkills._meta.fields]

    class Meta:
        model = DesignSkills

admin.site.register(DesignSkills, DesignSkillsAdmin)


class LanguageSkillsAdmin(admin.ModelAdmin):
    model = LanguageSkills
    list_display = [field.name for field in LanguageSkills._meta.fields]

    class Meta:
        model = LanguageSkills

admin.site.register(LanguageSkills, LanguageSkillsAdmin)


class InterestAdmin(admin.ModelAdmin):
    model = Interest
    list_display = [field.name for field in Interest._meta.fields]

    class Meta:
        model = Interest

admin.site.register(Interest, InterestAdmin)


class RefereancesAdmin(admin.ModelAdmin):
    model = Refereances
    list_display = [field.name for field in Refereances._meta.fields]

    class Meta:
        model = Refereances

admin.site.register(Refereances, RefereancesAdmin)


class OtherQualificationsAdmin(admin.ModelAdmin):
    model = OtherQualifications
    list_display = [field.name for field in OtherQualifications._meta.fields]

    class Meta:
        model = OtherQualifications

admin.site.register(OtherQualifications, OtherQualificationsAdmin)