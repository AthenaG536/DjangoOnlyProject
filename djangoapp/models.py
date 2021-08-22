from django.db import models


class AccountHolder(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('DOB')


class Risk(models.Model):
    created_by = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)
    risk_name = models.CharField(max_length=200)
    likelihood = models.IntegerField(default=0)