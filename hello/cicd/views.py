from django.conf import settings
import subprocess

from django.http import HttpResponse


def update_server(request):
    git = subprocess.run(
        ['git', 'pull'],
        cwd=settings.BASE_DIR,
    ).returncode
    if git == 0:
        try:
            touch = subprocess.run(
                ['touch', settings.WSGI_CONFIG]
            ).returncode
        except AttributeError:
            touch = 1

    return HttpResponse(
        f'{{"git": {git}, "touch": {touch}}}',
        status=200,
        content_type='application/json'
    )
