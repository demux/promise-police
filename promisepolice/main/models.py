# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


PROMISE_STATUS_CHOICES = (
    ('kept', 'Efnt'),
    ('not kept', 'Svikið'),
    ('unclear', 'Óljóst'),
)


class CommonModel(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, null=True, editable=False, related_name='+')
    modified_by = models.ForeignKey(User, null=True, editable=False, related_name='+')

    def save(self, commit=True):
        obj = super().save(commit=False)

        if obj.created_by:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user

        obj.save(commit=commit)

    class Meta:
        abstract = True


class Party(CommonModel):
    name = models.CharField(max_length=255)
    ident = models.CharField(max_length=10)
    about = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)


class Person(CommonModel):
    name = models.CharField(max_length=255)
    party = models.ForeignKey(Party, blank=True, null=True, related_name='members')
    ssn = models.CharField(max_length=50)
    about = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)


class Source(CommonModel):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True)
    about = models.TextField(blank=True)


class Promise(CommonModel):
    title = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    person = models.ForeignKey(Person, blank=True, null=True)
    party = models.ForeignKey(Party, blank=True, null=True, related_name='promises')
    dt_promised = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROMISE_STATUS_CHOICES)
    status_detail = models.TextField(blank=True)


class PromiseSource(CommonModel):
    promise = models.ForeignKey(Promise, related_name='sources')
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    detail = models.TextField(blank=True)


# class PromiseOccasion(CommonModel):
#     dt_promised = models.DateTimeField(blank=True, null=True)


# class Claim(models.Model):
#     pass
