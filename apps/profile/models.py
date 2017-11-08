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


class Locality(models.Model):
    human = models.ForeignKey(Profile)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=45)
    locality = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s" % (self.country, self.region, self.locality)


class WorkExperience(models.Model):
    human = models.ForeignKey(Profile)
    organization = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    work_start = models.DateField()
    work_end = models.DateField()
    description = models.TextField(blank=True ,null=True)


class EducationQualifications(models.Model):
    human = models.ForeignKey(Profile)
    education = models.CharField(max_length=150)
    school = models.CharField(max_length=200)
    study_start = models.DateField()
    study_end = models.DateField()
    some_text = models.TextField()


class DesignSkills(models.Model):
    human = models.ForeignKey(Profile)
    photoshop = models.IntegerField()
    illustrator = models.IntegerField()
    adobexd = models.IntegerField()
    sketch = models.IntegerField()
    indesign = models.IntegerField()
    imposition = models.IntegerField()


class LanguageSkills(models.Model):
    human = models.ForeignKey(Profile)
    language = models.CharField(max_length=100)


class Interest(models.Model):
    human = models.ForeignKey(Profile)
    interest = models.TextField(blank=True, null=True)


class Refereances(models.Model):
    human = models.ForeignKey(Profile)
    director = models.CharField(max_length=100)
    company = models.CharField(max_length=130)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

