from rest_framework import serializers

from ..models import Promise, Party, Person, PromiseSource, Source, PromiseSource


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'slug', 'ident', 'about', 'website',  'image_url',
                  'api_ref', 'ref')


class PersonSerializer(serializers.ModelSerializer):
    party = PartySerializer()

    class Meta:
        model = Person
        fields = ('name', 'slug', 'party', 'image_url', 'api_ref', 'ref',
                  'is_mp', 'is_substitute')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('name', 'url')


class PromiseSourceSerializer(serializers.ModelSerializer):
    source = SourceSerializer()

    class Meta:
        model = PromiseSource
        fields = ('dt_created', 'dt_modified', 'source', 'title', 'url', 'detail')


class PromiseSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    party = PartySerializer()
    sources = PromiseSourceSerializer(many=True, read_only=True)

    class Meta:
        model = Promise
        fields = ('dt_created', 'dt_modified', 'title', 'detail', 'person',
                  'party', 'dt_promised', 'status', 'status_detail', 'sources')
