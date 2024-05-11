from django.contrib import admin
from .models import Task, Label


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completion_status', 'owner', 'get_labels']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filter records based on the currently logged-in user
        return qs.filter(owner=request.user)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "labels":
            # Filter labels queryset based on the currently logged-in user
            kwargs["queryset"] = Label.objects.filter(owner=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_labels(self, obj):
        return ', '.join([label.name for label in obj.labels.all()])

    get_labels.short_description = 'Labels'

    def save_model(self, request, obj, form, change):
        # Set the owner of the task to the currently logged-in user
        if not obj.owner:
            obj.owner = request.user
        obj.save()


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filter records based on the currently logged-in user
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        # Set the owner of the task to the currently logged-in user
        if not obj.owner:
            obj.owner = request.user
        obj.save()