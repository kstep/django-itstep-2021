from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(
        max_length=200)

    def __str__(self):
        return f"Group #{self.pk} {self.name}"


class Student(models.Model):
    first_name = models.CharField(
        max_length=200)
    last_name = models.CharField(
        max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    birthday = models.DateField()
    room_number = models.IntegerField(null=True, default=None)

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