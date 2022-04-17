from datetime import datetime

import django.contrib.contenttypes.fields
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.base import ModelBase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, gettext


class Group(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    def __str__(self):
        return gettext("Group #{pk} {name}").format(
            pk=self.pk, name=self.name)


class Student(models.Model):
    first_name = models.CharField(
        _('First name'),
        max_length=200,
        validators=[RegexValidator(r'\s', inverse_match=True), ])

    last_name = models.CharField(
        _('Last name'),
        max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              verbose_name=_('Group'))
    birthday = models.DateField(_('Birthday'))
    room_number = models.IntegerField(_('Room number'), null=True, default=None)
    last_modified = models.DateTimeField(_('Last modified'), auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Student #{self.pk} {self.full_name} from group {self.group.name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    @property
    def url(self):
        return self.get_absolute_url()
