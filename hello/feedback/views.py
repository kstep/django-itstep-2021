import os.path

from django.conf import settings
from django.contrib import messages as msg
from django.contrib.messages import add_message, SUCCESS, get_messages, ERROR, error
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.template import Template
from django.template.loader import get_template
from django.views.generic import FormView

from feedback.forms import FeedbackForm


class SendFeedback(FormView):
    template_name = 'feedback/index.html'
    form_class = FeedbackForm
    success_url = 'send_feedback'

    def form_valid(self, form):
        pass


def send_feedback(request: HttpRequest):
    if request.method == 'GET':
        messages = get_messages(request)
        return render(request, 'feedback/index.html', {
            'form': FeedbackForm(),
        })

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if not form.is_valid():
            return render(request, 'feedback/index.html', {
                'form': form,
            })

        user_data = form.cleaned_data

        from django.core.mail import mail_managers, get_connection, send_mail
        with get_connection() as conn:
            tmpl = get_template('feedback/notify.txt')
            message_text = tmpl.render(user_data)
            mail_managers(f'Feed from user: {user_data["subject"]}',
                          message_text, connection=conn)

            tmpl = get_template('feedback/received.txt')
            message_text = tmpl.render(user_data)
            send_mail(
                f'Your message delivered: {user_data["subject"]}',
                message_text,
                from_email=settings.SERVER_EMAIL,
                recipient_list=[user_data['sender']],
                connection=conn)

        msg.error(request, 'Your message was successfully sent!')
        return redirect('send_feedback')