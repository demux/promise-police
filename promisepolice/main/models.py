# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


PROMISE_STATUS_CHOICES = (
    ('kept', 'Efnt'),
    ('not kept', 'Svikið'),
    ('unclear', 'Óljóst'),
)


class CommonModel(models.Model):
    dt_created = models.DateTimeField('Búið til', auto_now_add=True)
    dt_modified = models.DateTimeField('Breytt', auto_now=True)

    created_by = models.ForeignKey(User, verbose_name='Búið til af',
                                   null=True, editable=False, related_name='+')
    modified_by = models.ForeignKey(User, verbose_name='Breytt af',
                                    null=True, editable=False, related_name='+')

    # def save(self, commit=True, request=None):
    #     obj = super().save(commit=False)

    #     if request:
    #         if obj.created_by:
    #             obj.modified_by = request.user
    #         else:
    #             obj.created_by = request.user

    #     obj.save()

    class Meta:
        abstract = True


class Party(CommonModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    ident = models.CharField(max_length=10)
    about = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)

    image_url = models.URLField(max_length=255, blank=True)
    # http://api-dot-thingmenn.appspot.com/api/parties/piratar
    api_ref = models.URLField(max_length=255, blank=True)
    # http://thingmenn.is/thingflokkar/framsoknarflokkur
    ref = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return '%s (X%s)' % (self.name, self.ident)


class Person(CommonModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    party = models.ForeignKey(Party, blank=True, null=True, related_name='members')
    ssn = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)

    image_url = models.URLField(max_length=255, blank=True)
    # http://api-dot-thingmenn.appspot.com/api/parties/piratar
    api_ref = models.URLField(max_length=255, blank=True)
    # http://thingmenn.is/thingflokkar/framsoknarflokkur
    ref = models.URLField(max_length=255, blank=True)

    is_mp = models.BooleanField(default=True)
    is_substitute = models.BooleanField(default=False)

    def __str__(self):
        return '%s (X%s)' % (self.name, self.party.ident)


class Source(CommonModel):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Promise(CommonModel):
    title = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    person = models.ForeignKey(Person, blank=True, null=True)
    party = models.ForeignKey(Party, blank=True, null=True, related_name='promises')
    dt_promised = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROMISE_STATUS_CHOICES)
    status_detail = models.TextField(blank=True)

    def __str__(self):
        return self.title


class PromiseSource(CommonModel):
    promise = models.ForeignKey(Promise, related_name='sources')
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.url


# class PromiseOccasion(CommonModel):
#     dt_promised = models.DateTimeField(blank=True, null=True)


# class Claim(models.Model):
#     pass
