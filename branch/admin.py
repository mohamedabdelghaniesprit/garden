from django import forms
from django.contrib import admin
from feincms.admin import tree_editor
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from feincms.module.medialibrary.models import Category, MediaFile

from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch


class ActualBranchForm(BranchForm):
    def __init__(self, *args, **kwargs):
        super(ActualBranchForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Branch.objects.actual_list()


class BranchAdmin(tree_editor.TreeEditor):
    list_display = ('title', 'is_description', 'is_done',)
    form = BranchForm

    def is_description(self, branch):
        res = bool(branch.description or branch.qq)
        return res
    is_description.boolean = True
    is_description.short_description = 'Description/QQ'


class ProxyBranch(Branch):
    class Meta:
        verbose_name = 'Actual Branch'
        verbose_name_plural = 'Actual Branches'
        proxy = True


class ProxyBranchAdmin(tree_editor.TreeEditor):
    list_display = ('title', 'is_description',)
    form = ActualBranchForm

    def queryset(self, request):
        return self.model.objects.actual_list()

    def is_description(self, branch):
        res = bool(branch.description or branch.qq)
        return res
    is_description.boolean = True
    is_description.short_description = 'Description/QQ'


admin.site.register(ProxyBranch, ProxyBranchAdmin)
admin.site.register(Branch, BranchAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Category)
admin.site.unregister(MediaFile)
