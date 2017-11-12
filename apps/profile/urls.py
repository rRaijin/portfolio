from django.conf.urls import url
from apps.profile import views

urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name="main"),
    url(r'^profile/(?P<id>[\d-]+)/$', views.profile, name="user_profile"),

    url(r'^profile_edit/(?P<id>[\d-]+)/$', views.EditProfile.as_view(), name="profile-edit"),
    # url(r'^skill_edit/(?P<id>[\d-]+)/$', views.EditSkill.as_view(), name="skill-edit"),

    url(r'^lang_add/(?P<id>[\d-]+)/$', views.AddLang.as_view(), name="lang-add"),
    url(r'^lang_edit/(?P<id>[\d-]+)/$', views.EditLang.as_view(), name="lang-edit"),
    url(r'^lang_del/(?P<id>[\d-]+)/$', views.DeleteLang.as_view(), name="lang-del"),

    url(r'^ref_add/(?P<id>[\d-]+)/$', views.AddRef.as_view(), name="ref-add"),
    url(r'^ref_edit/(?P<id>[\d-]+)/$', views.EditRef.as_view(), name="ref-edit"),
    url(r'^ref_del/(?P<id>[\d-]+)/$', views.DeleteRef.as_view(), name="ref-del"),

    url(r'^workexp_add/(?P<id>[\d-]+)/$', views.AddWorkExperience.as_view(), name="work-exp-add"),
    url(r'^workexp_edit/(?P<id>[\d-]+)/$', views.EditWorkExperience.as_view(), name="work-exp-edit"),
    url(r'^workexp_del/(?P<id>[\d-]+)/$', views.DeleteWorkExperience.as_view(), name="work-exp-del"),

    url(r'^education_add/(?P<id>[\d-]+)/$', views.AddEducation.as_view(), name="education-add"),
    url(r'^education_edit/(?P<id>[\d-]+)/$', views.EditEducation.as_view(), name="education-edit"),
    url(r'^education_del/(?P<id>[\d-]+)/$', views.DeleteEducation.as_view(), name="education-del"),

    url(r'^other_add/(?P<id>[\d-]+)/$', views.AddOther.as_view(), name="other-add"),
    url(r'^other_edit/(?P<id>[\d-]+)/$', views.EditOther.as_view(), name="other-edit"),
    url(r'^other_del/(?P<id>[\d-]+)/$', views.DeleteOther.as_view(), name="other-del"),
]