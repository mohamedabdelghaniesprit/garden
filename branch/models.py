from django.db import models
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel


class BranchManager(TreeManager):
    def actual_list(self):
        return self.get_queryset().filter(is_done=False)


class Branch(MPTTModel):
    is_done = models.BooleanField('Is done', default=False)
    title = models.CharField('Title', max_length=255)
    parent = TreeForeignKey('self', verbose_name='Parent', related_name='children', blank=True, null=True)
    qq = models.TextField('QQ', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)

    objects = BranchManager()

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'All Branches'

    def __unicode__(self):
        return self.title
