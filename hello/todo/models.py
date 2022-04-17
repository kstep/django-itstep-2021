from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(_("Task description"),
                                   max_length=500)
    is_done = models.BooleanField(_("Is task done"),
                                  default=False)
    created_date = models.DateTimeField(_("Task create date"),
                                        auto_now_add=True)
    complete_date = models.DateTimeField(_("Task complete date"),
                                         blank=True,
                                         null=True,
                                         default=None)

    def __str__(self):
        return f'{self.description} ({self.is_done})'

