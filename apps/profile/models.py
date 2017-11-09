from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(help_text="age must be positive")
    photo = models.ImageField(upload_to='people_photos/')
    email = models.EmailField(unique=True)
    website = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    statement = models.TextField()

    def __str__(self):
        return "%s %s" % (self.last_name, self.user_name)

    def full_name(self):
        return "%s %s" % (self.user_name, self.last_name)


class Locality(models.Model):
    human = models.ForeignKey(Profile)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=45)
    locality = models.CharField(max_length=100)

    def full_locality(self):
        return "%s,%s,%s" % (self.country, self.region, self.locality)


class WorkExperience(models.Model):
    human = models.ForeignKey(Profile)
    organization = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    work_start = models.DateField()
    work_end = models.DateField()
    description = models.TextField(blank=True ,null=True)

    def __str__(self):
        return self.organization

    def work_duration(self):
        return "%s-%s" % (self.work_start, self.work_end)


class EducationQualifications(models.Model):
    human = models.ForeignKey(Profile)
    education = models.CharField(max_length=150)
    school = models.CharField(max_length=200)
    study_start = models.DateField()
    study_end = models.DateField()
    some_text = models.TextField()

    def __str__(self):
        return self.education

    def education_duration(self):
        return "%s-%s" % (self.study_start, self.study_end)


class DesignSkills(models.Model):
    human = models.ForeignKey(Profile)
    photoshop = models.IntegerField(help_text="sss")
    illustrator = models.IntegerField()
    adobexd = models.IntegerField()
    sketch = models.IntegerField()
    indesign = models.IntegerField()
    imposition = models.IntegerField()


class LanguageSkills(models.Model):
    human = models.ForeignKey(Profile)
    language = models.CharField(max_length=100)
    #level = models.CharField(max_length=50)

    def __str__(self):
        return self.language


class Interest(models.Model):
    human = models.ForeignKey(Profile)
    interest = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.interest


class Refereances(models.Model):
    human = models.ForeignKey(Profile)
    director = models.CharField(max_length=100)
    company = models.CharField(max_length=130)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.director


class OtherQualifications(models.Model):
    human = models.ForeignKey(Profile)
    qualification = models.CharField(max_length=100)
    web_sourse = models.CharField(max_length=100)
    some_start = models.DateField()
    some_end = models.DateField()
    some_text = models.TextField()

    def __str__(self):
        return self.qualification

    def other_duration(self):
        return "%s to %s" % (self.some_start, self.some_end)

