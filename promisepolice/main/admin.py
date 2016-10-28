from django.contrib import admin
from .models import *


class SourceInline(admin.StackedInline):
    model = PromiseSource


@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):
    inlines = (SourceInline,)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
