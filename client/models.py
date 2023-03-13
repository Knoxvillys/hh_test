from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Applicant(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=60)
    phoneNumber = PhoneNumberField(unique=True, null=False, blank=False)
    secondPhoneNumber = PhoneNumberField(null=True, blank=True)
    about_me = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image', null=True)
    salary = models.IntegerField(null=True)
    company = models.CharField(max_length=100)
    results_of_work = models.CharField(max_length=600)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Автор')

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
