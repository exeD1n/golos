from django.contrib import admin
from .models import All, Group, CourseOfStudy, Hilary, Item


# Register your models here.
@admin.register(All)
class AllAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'mail', 'formOfStudy', 'group', 'courseOfStudy', 'hilary_id', 'item')
    list_filter = ('fullName', 'formOfStudy', 'group', 'courseOfStudy', 'hilary_id', 'item')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'directionStudy')
    list_filter = ('name', 'directionStudy')

admin.site.register(CourseOfStudy)
admin.site.register(Hilary)
admin.site.register(Item)