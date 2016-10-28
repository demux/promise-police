from django.contrib import admin

from pagedown.widgets import AdminPagedownWidget

from .models import *


class ModelAdminMixin:
    readonly_fields = ('dt_created', 'dt_modified', 'created_by', 'modified_by')

    formfield_overrides = {
        models.TextField: {
            'widget': AdminPagedownWidget
        }
    }

    def save_model(self, request, obj, form, change):
        if request:
            if obj.created_by:
                obj.modified_by = request.user
            else:
                obj.created_by = request.user
        obj.save()


class ModelAdmin(ModelAdminMixin, admin.ModelAdmin):
    pass


class SourceInline(ModelAdminMixin, admin.StackedInline):
    model = PromiseSource
    extra = 0


@admin.register(Promise)
class PromiseAdmin(ModelAdmin):
    inlines = (SourceInline,)


class ClaimSourceInline(ModelAdminMixin, admin.StackedInline):
    model = ClaimSource
    extra = 0


@admin.register(Claim)
class ClaimAdmin(ModelAdmin):
    inlines = (ClaimSourceInline,)


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    pass


@admin.register(Party)
class PartyAdmin(ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(ModelAdmin):
    pass
