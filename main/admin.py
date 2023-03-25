from django.contrib import admin
from .models import All, Group, CourseOfStudy, Hilary


# Register your models here.
@admin.register(All)
class AllAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'mail', 'formOfStudy', 'group', 'courseOfStudy', 'hilary_id')
    list_filter = ('fullName', 'formOfStudy', 'group', 'courseOfStudy', 'hilary_id')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'directionStudy')
    list_filter = ('name', 'directionStudy')

admin.site.register(CourseOfStudy)
admin.site.register(Hilary)