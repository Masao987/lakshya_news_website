from django.contrib import admin
from crowdfunding.models import Project, Pledge, ProjectImage, ProjectUpdate
# from mce_filebrowser.admin import MCEFilebrowserAdmin


# Register your models here.


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fields = ('image', 'show_thumbnail')
    readonly_fields = ('show_thumbnail',)


class ProjectUpdate(admin.TabularInline):
    model = ProjectUpdate
    fields = ('author', 'update', 'mail_status')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'goal', 'get_percentage_pledged', 'days_remaining', 'mail_status')
    inlines = (ProjectImageInline, ProjectUpdate,)
    search_fields = ('title',)


class PledgeAdmin(admin.ModelAdmin):
    list_display = ('project', 'amount', 'user', 'pledge_fulfilled')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Pledge, PledgeAdmin)
