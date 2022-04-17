from celery import shared_task


@shared_task
def send_email_messages(emails):
    print(f"Sending emails to {emails}")