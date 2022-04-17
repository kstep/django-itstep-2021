from logging import getLogger

from django.core.management import BaseCommand
from django.db.models.signals import pre_save
from django.dispatch import Signal
from django.utils import timezone

from students import models

birthday_email_pre_send = Signal()
birthday_email_post_send = Signal()

logger = getLogger(__name__)


class Command(BaseCommand):
    help = 'send emails for students'

    def handle(self, *args, **options):
        today = timezone.now().date()

        # students = models.Student.filter(birthday=today)
        students = models.Student.objects.all()

        for student in students:
            birthday_email_pre_send \
                .send(self.__class__, instance=student)

            print(student)
            # send_mail()

            birthday_email_post_send \
                .send(self.__class__, instance=student)


def pre_send_handler(sender, instance, **kwargs):
    logger.info("Going to send birthday email to student id=%s",
                instance.pk)

birthday_email_pre_send.connect(pre_send_handler, Command)
