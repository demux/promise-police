from django.contrib import admin

from pagedown.widgets import AdminPagedownWidget
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import *


class ModelAdminMixin:
    readonly_fields = ('dt_created', 'dt_modified', 'created_by', 'modified_by')

    formfield_overrides = {
        models.TextField: {
            'widget': AdminPagedownWidget
        }
    }

    def save_model(self, request, obj, form, change):
        if obj.created_by:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
        obj.save()


class ModelAdmin(ModelAdminMixin, admin.ModelAdmin):
    pass
    # def save_formset(self, request, form, formset, change):
    #     for form in formset.forms:
    #         obj = form.instance
    #         if hasattr(obj, 'user'):
    #             if not change:
    #                 obj.user = request.user
    #         elif hasattr(obj, 'created_by'):
    #             if change:
    #                 obj.modified_by = request.user
    #             else:
    #                 obj.created_by = request.user
    #         obj.save()


class SourceInline(ModelAdminMixin, admin.StackedInline):
    model = PromiseSource
    extra = 0


class NoteInline(ModelAdminMixin, GenericStackedInline):
    readonly_fields = ('dt_created', 'dt_modified', 'user')
    model = Note
    extra = 0

    def save_model(self, request, obj, form, change):
        print('asdf')
        obj.save()


@admin.register(Promise)
class PromiseAdmin(ModelAdmin):
    inlines = (SourceInline, NoteInline)


class ClaimSourceInline(ModelAdminMixin, admin.StackedInline):
    model = ClaimSource
    extra = 0


@admin.register(Claim)
class ClaimAdmin(ModelAdmin):
    inlines = (ClaimSourceInline, NoteInline)
    filter_horizontal = ('persons_accused', 'parties_accused')


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    pass


@admin.register(Party)
class PartyAdmin(ModelAdmin):
    pass


@admin.register(Source)
class SourceAdmin(ModelAdmin):
    pass
