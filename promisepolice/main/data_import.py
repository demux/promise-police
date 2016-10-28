import requests
from django.utils.text import slugify

from .models import Party, Person



site_url = 'http://thingmenn.is'

def import_parties():
    base_url = 'http://api-dot-thingmenn.appspot.com/api/parties'
    res = requests.get(base_url)
    parties = res.json()

    for data in parties:
        url = '%s/%s' % (base_url, data['id'])
        slug = slugify(data['id'])

        try:
            party = Party.objects.get(slug=slug)
        except Party.DoesNotExist:
            party = Party()

        party.slug = slug
        party.ref = '%s/thingflokkar/%s' % (site_url, data['id'])
        party.api_ref = '%s/%s' % (base_url, data['id'])

        party.name = data['name']
        party.about = data['about']
        party.image_url = ''.join([site_url, data['imagePath']])

        party.save()



def import_mps():
    base_url = 'http://api-dot-thingmenn.appspot.com/api/mps'
    res = requests.get(base_url)
    mps = res.json()

    for mp in mps:
        url = '%s/%s' % (base_url, mp['id'])

        # Make sure slugs are correctly formatted:
        slug = slugify(mp['slug'].replace('_', '-'))

        try:
            person = Person.objects.get(slug=slug)
        except Person.DoesNotExist:
            person = Person()

        person.ref = '%s/thingmenn/%s' % (site_url, mp['id'])
        person.api_ref = '%s/%s' % (base_url, mp['id'])

        person.name = mp['name']
        person.slug = slug
        person.about = mp['description']
        person.party = Party.objects.get(slug=slugify(mp['partySlug']))
        person.image_url = mp['imagePath']

        person.is_mp = True
        person.is_substitute = mp['isSubstitute']

        person.save()
