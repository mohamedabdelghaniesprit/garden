from django.contrib import admin
from feincms.admin import tree_editor
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from feincms.module.medialibrary.models import Category, MediaFile

from .models import Branch


class BranchAdmin(tree_editor.TreeEditor):
    list_display = ('title', 'is_done',)


class ProxyBranch(Branch):
    class Meta:
        verbose_name = 'Actual Branch'
        verbose_name_plural = 'Actual Branches'
        proxy = True


class ProxyBranchAdmin(BranchAdmin):
    def queryset(self, request):
        return self.model.objects.actual_list()


admin.site.register(ProxyBranch, ProxyBranchAdmin)
admin.site.register(Branch, BranchAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Category)
admin.site.unregister(MediaFile)
