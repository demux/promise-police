from django.contrib import admin
from .models import *


class SourceInline(admin.StackedInline):
    model = PromiseSource


class ModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if request:
            if obj.created_by:
                obj.modified_by = request.user
            else:
                obj.created_by = request.user
        obj.save()


@admin.register(Promise)
class PromiseAdmin(ModelAdmin):
    inlines = (SourceInline,)


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    pass


@admin.register(Party)
class PartyAdmin(ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(ModelAdmin):
    pass
