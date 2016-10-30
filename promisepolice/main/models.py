# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


PROMISE_STATUS_CHOICES = (
    ('kept', 'Efnt'),
    ('not kept', 'Svikið'),
    ('unclear', 'Óljóst'),
)


TRUTHFULNESS_CHOICES = (
    ('True', 'Dagsatt'),
    ('Mostly True', 'Næstum því satt'),
    ('Half True', 'Hálfsannleikur'),
    ('Mostly False', 'Aðallega ósatt'),
    ('False', 'Haugalýgi'),
)


class CommonModel(models.Model):
    dt_created = models.DateTimeField('Búið til', auto_now_add=True)
    dt_modified = models.DateTimeField('Breytt', auto_now=True)

    created_by = models.ForeignKey(User, verbose_name='Búið til af',
                                   null=True, editable=False, related_name='+')
    modified_by = models.ForeignKey(User, verbose_name='Breytt af',
                                    null=True, editable=False, related_name='+')

    class Meta:
        abstract = True


class Party(CommonModel):
    name = models.CharField('Nafn', max_length=255)
    slug = models.SlugField(blank=True)
    ident = models.CharField('Stafur', max_length=10)
    about = models.TextField('Um flokkinn', blank=True)
    website = models.URLField('Vefur', max_length=255, blank=True)

    image_url = models.URLField('Mynd', max_length=255, blank=True)
    # http://api-dot-thingmenn.appspot.com/api/parties/piratar
    api_ref = models.URLField('API tilvísun', max_length=255, blank=True)
    # http://thingmenn.is/thingflokkar/framsoknarflokkur
    ref = models.URLField('Tilvísun', max_length=255, blank=True)

    def __str__(self):
        return '%s (X%s)' % (self.name, self.ident)

    class Meta:
        verbose_name = 'Flokkur'
        verbose_name_plural = 'Flokkar'


class Person(CommonModel):
    name = models.CharField('Nafn', max_length=255)
    slug = models.SlugField(blank=True)
    party = models.ForeignKey(Party, blank=True, null=True, related_name='members')
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

    class Meta:
        verbose_name = 'Aðili'
        verbose_name_plural = 'Aðilar'


class Source(CommonModel):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Miðill'
        verbose_name_plural = 'Miðlar'


class Promise(CommonModel):
    title = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    person = models.ForeignKey(Person, blank=True, null=True, related_name='promises')
    party = models.ForeignKey(Party, blank=True, null=True, related_name='promises')
    dt_promised = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=PROMISE_STATUS_CHOICES)
    status_detail = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Loforð'
        verbose_name_plural = 'Loforð'


class AbstractSource(CommonModel):
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Heimild'
        verbose_name_plural = 'Heimildir'
        abstract = True


class PromiseSource(AbstractSource):
    promise = models.ForeignKey(Promise, related_name='sources')


class Claim(CommonModel):
    title = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    person = models.ForeignKey(Person, blank=True, null=True, related_name='claims')
    party = models.ForeignKey(Party, blank=True, null=True, related_name='claims')
    dt_claimed = models.DateTimeField(blank=True, null=True)
    truthfulness = models.CharField('Sannleiksgildi', max_length=50, choices=TRUTHFULNESS_CHOICES)

    persons_accused = models.ManyToManyField(Person, verbose_name='Ásakaðir aðilar',
                                             related_name='accused_by_claims', blank=True)
    parties_accused = models.ManyToManyField(Party, verbose_name='Ásakapir flokkar',
                                             related_name='accused_by_claims', blank=True)

    the_truth = models.TextField('Sannleikurinn', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Fullyrðing'
        verbose_name_plural = 'Fullyrðingar'


class ClaimSource(AbstractSource):
    claim = models.ForeignKey(Claim, related_name='sources')
