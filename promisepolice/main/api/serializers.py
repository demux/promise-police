from rest_framework import serializers

from ..models import Promise, Party, Person


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'dt_created', 'dt_modified', 'name', 'slug', 'ident',
                  'about', 'website',  'image_url', 'api_ref', 'ref')


class PersonSerializer(serializers.ModelSerializer):
    party = PartySerializer()

    class Meta:
        model = Person
        fields = ('id', 'dt_created', 'dt_modified', 'name', 'slug', 'party',
            'ssn', 'about', 'website', 'image_url', 'api_ref', 'ref', 'is_mp',
            'is_substitute')


class PromiseSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    party = PartySerializer()

    class Meta:
        model = Promise
        fields = ('id', 'dt_created', 'dt_modified', 'title', 'detail', 'person',
                  'party', 'dt_promised', 'status', 'status_detail')
